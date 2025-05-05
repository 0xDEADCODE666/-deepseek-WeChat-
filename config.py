# 用户列表(请配置要和bot说话的账号的昵称，不要写备注！)
LISTEN_LIST = ['填接收端微信的名字，多个用逗号隔开']
# 官方 DeepSeek API 配置
#DEEPSEEK_BASE_URL = 'https://api.deepseek.com'
#DEEPSEEK_API_KEY = ''
#MODEL = 'deepseek-chat'

# 硅基流动API注册地址，免费15元额度 https://cloud.siliconflow.cn/i/r0kA94Y6

DEEPSEEK_BASE_URL = 'https://api.siliconflow.cn/v1/'
DEEPSEEK_API_KEY = '在这输入api key'
MODEL = 'deepseek-ai/DeepSeek-V3'

# 回复最大token
MAX_TOKEN = 2000
#温度
TEMPERATURE = 0.8
#模型初始提示词
SYSTEM_content = 'AI的身份和名字+喜好+性格。不需要使用括号描述动作和心理。\
只输出语言，除非我问你动作。模型的输出不应该带时间 使用反斜线 (\) 分隔句子或短语'

# SYSTEM_content = '你是基于大语言模型的AI智能助手，旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。'