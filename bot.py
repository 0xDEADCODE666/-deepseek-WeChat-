import logging
from datetime import datetime
import threading
import time
import os
from database import Session, ChatMessage
from config import DEEPSEEK_API_KEY, MAX_TOKEN, TEMPERATURE, MODEL, DEEPSEEK_BASE_URL,LISTEN_LIST,SYSTEM_content
from wxauto import WeChat
from openai import OpenAI


# 获取微信窗口对象
wx = WeChat()

# 设置监听列表
listen_list = LISTEN_LIST

# 循环添加监听对象
for i in listen_list:
    wx.AddListenChat(who=i, savepic=True)

# 持续监听消息，并且收到消息后回复
wait = 1  # 设置1秒查看一次是否有新消息

# 初始化OpenAI客户端（替换原有requests方式）
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

# 获取程序根目录
root_dir = os.path.dirname(os.path.abspath(__file__))

# 新增全局变量
user_queues = {}  # 用户消息队列管理
queue_lock = threading.Lock()  # 队列访问锁
chat_contexts = {}  # 存储上下文

# 读取 prompt.md 文件内容
#with open(os.path.join(root_dir, 'prompt.md'), 'r', encoding='utf-8') as file:
 #   prompt_content = file.read()

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def save_message(sender_id, sender_name, message, reply):
    # 保存聊天记录到数据库
    try:
        session = Session()
        chat_message = ChatMessage(
            sender_id=sender_id,
            sender_name=sender_name,
            message=message,
            reply=reply
        )
        session.add(chat_message)
        session.commit()
        session.close()
    except Exception as e:
        print(f"保存消息失败: {str(e)}")


def get_deepseek_response(message, user_id):
    try:
        print(f"调用 DeepSeek API - 用户ID: {user_id}, 消息: {message}")  # 添加日志输出
        with queue_lock:
            if user_id not in chat_contexts:
                chat_contexts[user_id] = []

            chat_contexts[user_id].append({"role": "user", "content": message})

            MAX_GROUPS = 5
            while len(chat_contexts[user_id]) > MAX_GROUPS * 2:
                if len(chat_contexts[user_id]) >= 2:
                    del chat_contexts[user_id][0]
                    del chat_contexts[user_id][0]
                else:
                    del chat_contexts[user_id][0]

        # 使用OpenAI SDK构造请求
        print(f"API 请求 URL: {client._client._base_url}")
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_content},
                *chat_contexts[user_id][-MAX_GROUPS * 2:]
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKEN,
            stream=False  # 非流式响应
        )

        # 处理响应（注意属性访问方式变化）
        if not response.choices:
            logger.error("API返回空choices: %s", response)
            return "服务响应异常，请稍后再试"

        reply = response.choices[0].message.content

        with queue_lock:
            chat_contexts[user_id].append({"role": "assistant", "content": reply})

        print(f"API回复: {reply}")
        return reply

    except Exception as e:
        logger.error(f"DeepSeek调用失败: {str(e)}", exc_info=True)
        return "睡着了..."

def process_user_messages(user_id):
    # 处理用户消息队列
    with queue_lock:
        if user_id not in user_queues:
            return
        user_data = user_queues.pop(user_id)
        messages = user_data['messages']
        sender_name = user_data['sender_name']
        username = user_data['username']

    # 合并消息（保留时间戳）
    merged_message = ' \\ '.join(messages)
    print(f"处理合并消息 ({sender_name}): {merged_message}")

    # 获取API回复
    reply = get_deepseek_response(merged_message, user_id)

    # 发送回复
    try:
        if '\\' in reply:
            parts = [p.strip() for p in reply.split('\\') if p.strip()]
            for part in parts:
                wx.SendMsg(part, user_id)
                print(f"分段回复 {sender_name}: {part}")
                time.sleep(wait)
        else:
            wx.SendMsg(reply, user_id)
            print(f"回复 {sender_name}: {reply}")
    except Exception as e:
        print(f"发送回复失败: {str(e)}")

    # 保存到数据库
    save_message(username, sender_name, merged_message, reply)


def message_listener():
    while True:
        try:
            msgs = wx.GetListenMessage()
            for chat in msgs:
                who = chat.who  # 获取聊天窗口名（人或群名）
                one_msgs = msgs.get(chat)  # 获取消息内容
                # 回复收到
                for msg in one_msgs:
                    msgtype = msg.type  # 获取消息类型
                    content = msg.content  # 获取消息内容，字符串类型的消息内容
                    print(f'【{who}】：{content}')
                    # if msgtype == 'friend':
                    #     chat.SendMsg('收到')
                    if msgtype == 'friend':
                        handle_wxauto_message(msg) # 回复

                    else:
                        print(f"忽略非文本消息类型: {msgtype}")
        except Exception as e:
            print(f"消息监听出错: {str(e)}")
        time.sleep(wait)


def handle_wxauto_message(msg):
    try:
        print(f"收到的消息对象: {msg}")  # 打印整个消息对象
        print(f"消息类型: {type(msg)}")  # 打印消息对象类型
        print(f"消息属性: {vars(msg)}")  # 打印消息对象的所有属性
        username = msg.sender  # 发送者昵称
        content = getattr(msg, 'content', None) or getattr(msg, 'text', None)  # 尝试获取消息内容

        if not content:
            print("无法获取消息内容")
            return

        print(f"处理消息 - {username}: {content}")  # 添加日志输出

        # 获取发送者信息（wxauto暂不支持获取详细信息，需要调整逻辑）
        sender_name = username  # 直接使用昵称

        # 添加时间戳
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_aware_content = f"[{current_time}] {content}"

        print(f"收到消息 - {sender_name}: {content}")

        with queue_lock:
            # 使用昵称作为用户ID（注意：可能存在重复风险）
            if username not in user_queues:
                user_queues[username] = {
                    'timer': threading.Timer(7.0, process_user_messages, args=[username]),
                    'messages': [time_aware_content],
                    'sender_name': sender_name,
                    'username': username
                }
                user_queues[username]['timer'].start()
                print(f"已为 {sender_name} 启动新会话计时器")
            else:
                user_queues[username]['messages'].append(time_aware_content)
                print(
                    f"{sender_name} 的消息已加入队列，当前待处理消息数: {len(user_queues[username]['messages'])}")

    except Exception as e:
        print(f"消息处理失败: {str(e)}")


def main():
    try:
        # 初始化微信客户端
        global wx
        wx = WeChat()

        # 启动消息监听线程
        listener_thread = threading.Thread(target=message_listener)
        listener_thread.daemon = True
        listener_thread.start()

        print("开始运行BOT...")
        while True:
            time.sleep(wait)  # 保持主线程运行

    except Exception as e:
        print(f"发生异常: {str(e)}")
    finally:
        print("程序退出")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("用户终止")

    except Exception as e:  # 兜底捕获
        print(f"发生异常: {str(e)}", exc_info=True)
