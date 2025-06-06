![ATRI.jpg](img%2FATRI.jpg)

---
## Introduction
English · [简体中文](./README.md) 
- My Dream Moments is an emotional companion program based on a large language model (LLM) that can connect to WeChat, providing a more authentic emotional interaction experience. It features the Atri-My Dear Moments prompt and addresses the rigid question-and-answer format of traditional human-machine dialogue, offering immersive role-playing and multi-turn conversation support. The project name stems from the original title of the first intelligent agent running on this program combined with the project's core values.
- It is recommended to use the DeepSeek V3 model.  
  ![demo.png](img%2Fdemo.png)

---

## Disclaimer
- This project is intended solely for educational and communication purposes. Statements made by the LLM do not represent the author's views. The copyright for the characters mimicked by the prompts belongs to the original creators. Any unauthorized activities deemed inappropriate will be the sole responsibility of the user.

---

## Implemented Features
- [x] Integration with WeChat for immersive role-playing
- [x] Segmented response in chats to eliminate the human-machine feel
- [x] Multi-turn dialogue
- [x] Support for multiple users
- [x] Prompts generated by DeepSeek R1 utilizing game text
- [x] Time awareness without internet connectivity

---

## Upcoming Features – We Welcome Your Contributions
- [ ] Scheduled tasks and intelligent scheduling
- [ ] Utilizing an 8B small model to generate memories in real-time and periodically organize them, allowing for persistent memory
- [ ] WebUI for user configuration without needing to understand code
- [ ] Load balancing
- [ ] Releases

---

## How to Run the Project
### 1. Preparations
1. **Spare Phone/Android Emulator**  
   - The WeChat desktop client must be logged in simultaneously on a mobile device, so using your primary device is not advisable.
2. **WeChat Secondary Account**  
   - You need to register an older WeChat account (newly registered accounts may not be able to log in as a bot). If you encounter an error after scanning, please check this requirement.
3. **DeepSeek API Key**  
   - It is recommended to obtain it from: [Get API Key (15 yuan free quota)](https://cloud.siliconflow.cn/i/aQXU6eC5)

---

### 2. Deploy the Project
1. **Clone this Repository**  
   ```bash
   git clone <repository_address>
   ```
2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure `config.py`**  
   Modify `DEEPSEEK_API_URL` and `DEEPSEEK_API_KEY`. Adjust `MAX_TOKEN`, `TEMPERATURE`, and `MODEL` as needed.
4. **Run `bot.py`**  
   ```bash
   python bot.py
   ```

### 3. How to Use
1. **After running the project, a `QR.png` will be generated in the root directory.**
   - Use this QR code to log in with the WeChat account you want to use as a bot.
   - If there is no response in the console, please restart the project to refresh the QR code and try logging in again.
2. **When the console displays `Start auto replying.`, it indicates that the program is running successfully. You can now test the bot by chatting with it on WeChat.**

## Modifying the Prompt
- The `prompt.md` file in the project root directory can be edited to modify prompts. Changes will take effect upon restarting the project.
- Note: Please do not alter prompts related to the backslash `\`, as they are utilized for segmented message replies.

## Sponsorship
This project welcomes sponsorship. Your support is very important to me!
- Sponsored users interested in remote deployment or custom prompts, please contact me.
- E-Mail: yangchenglin2004@foxmail.com
- Bilibili: [umaru今天吃什么](https://space.bilibili.com/209397245)
- Thank you for your support and usage!  
  ![qrcode.jpg](img%2Fqrcode.jpg)