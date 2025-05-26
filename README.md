![ATRI.jpg](img%2FATRI.jpg)

---
## 简介
简体中文 · [English](./README_EN.md) 
- 使用教程：[不封号！90秒让DeepSeek沉浸式接入微信变成你的Ai老婆](https://www.bilibili.com/video/BV1XCPSehEif/)
- 已经更换了安全的微信自动化方案，即<code>wxauto</code>，封号可能性几乎没有，稳定性拉满
- My Dream Moments 是一个基于大型语言模型（LLM）的情感陪伴程序，能够接入微信，提供更真实的情感交互体验。内置了 Atri-My dear moments 的 prompt，并且解决了传统人机对话程序一问一答的死板效果，提供沉浸式角色扮演和多轮对话支持。项目名字来源是运行在该程序上的第一个智能体的原作名称+项目价值观混合而来。
- 推荐使用DeepSeek V3 模型。<br>
![demo.png](img%2Fdemo.png)
---

## 已实现的功能
- [x] 对接微信，沉浸式角色扮演
- [x] 聊天分段响应，消除人机感
- [x] 多轮对话
- [x] 多用户支持
- [x] 由 DeepSeek R1 利用游戏文本生成的 Prompt
- [x] 无需联网的时间感知

---

## 待实现功能，期待您的加入
- [ ] 定时任务与智能定时任务
- [ ] 利用 8B 小模型实时生成记忆并定期整理，实现持久记忆
- [ ] WebUI，方便不理解代码的用户配置项目
- [ ] 负载均衡
- [ ] Releases

---

## 如何运行项目

### 1. 前期准备
1. **备用手机/安卓模拟器**  
   - 微信电脑端登录必须有一个移动设备同时登录，因此不能使用您的主要设备。
   
2. **微信小号**  
   - 可以登录微信电脑版即可。

3. **DeepSeek API Key**  
   - 推荐使用：[获取 API Key（15元免费额度）](https://cloud.siliconflow.cn/i/aQXU6eC5)

4. **(可选)云电脑或Windows Server**  
   - 因为wxauto需要前台运行，所以最好有一台云电脑或Windows Server
---

### 2. 部署项目
1. **克隆本仓库**  
   ```bash
   git clone <仓库地址>
2. **安装依赖**  
   ```bash
   pip install -r requirements.txt
3. **配置<code>config.py</code>**  
修改<code>LISTEN_LIST</code>、<code>DEEPSEEK_BASE_URL</code>和<code>DEEPSEEK_API_KEY</code>。
按需调整<code>MAX_TOKEN</code>、<code>TEMPERATURE</code>和<code>MODEL</code>。如何配置请阅读<code>config.py</code>里的注释。
4. **运行<code>bot.py</code>，如果报错请尝试使用Python 3.11版本。**
   ```bash
   python bot.py

### 3. 如何使用
- **项目运行后，控制台提示**
     ```bash
   初始化成功，获取到已登录窗口：<您的微信昵称>
   开始运行BOT...
即可开始监听并调用模型自动回复消息。
## 如果您想修改prompt
- 项目根目录下的 <code>prompt.md</code> 可以编辑，修改后重启项目生效。
- 注意：请不要修改与反斜线 <code> \ </code>相关的 prompt，因为它们被用于分段回复消息。
## 赞助
此项目欢迎赞助。您的支持对我非常重要！
- 赞助用户如需远程部署或定制 prompt，请联系我。
- E-Mail: yangchenglin2004@foxmail.com 
- Bilibili: [umaru今天吃什么](https://space.bilibili.com/209397245)
- 感谢您的支持与使用！!<br>
![qrcode.jpg](img%2Fqrcode.jpg)

