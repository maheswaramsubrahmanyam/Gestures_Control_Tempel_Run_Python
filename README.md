# 🖐️ Gesture Controlled Game Bot 🎮

Control your favorite games with just your hand gestures using **Python**, **OpenCV**, and **MediaPipe**.  
This bot simulates keyboard inputs based on real-time hand tracking and works seamlessly with browser games like **Subway Surfers on Poki.com**.

---

## 📽️ Demo

[![Watch the demo]([https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg](https://youtu.be/tU3b43tUR5Y))]([https://www.youtube.com/watch?v=YOUR_VIDEO_ID](https://youtu.be/tU3b43tUR5Y))

---

## ✨ Features

- 🔴 Real-time hand tracking via webcam  
- 🎮 Hands-free gaming with gesture controls  
- 💡 Lightweight, beginner-friendly codebase  
- ⏱️ Cooldown system to avoid repeated triggers  
- 🛠️ Easily customizable for any game or gesture set  

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/maheswaram-mv/gesture-game-bot.git
cd gesture-game-bot

# Install dependencies
pip install opencv-python mediapipe pyautogui

```
**▶️ Run the Project**
```bash

python game.py

```
**⚠️ IMPORTANT:** Keep the game window focused (e.g., Subway Surfers in browser) after running the script.

**🧠 How It Works**
🎥 Captures webcam feed using OpenCV

🖐️ Uses MediaPipe to detect hand landmarks

✌️ Classifies gestures by analyzing finger positions

⌨️ Triggers keyboard presses via PyAutoGUI

## ✋ Supported Gestures

| Gesture        | Action      | Key Press |
|----------------|-------------|-----------|
| ✊ Fist         | Slide       | ⬇️ Down   |
| ☝️ Index Only  | Jump        | ⬆️ Up     |
| ✌️ Peace Sign  | Move Right  | ➡️ Right  |
| 👌 OK Sign     | Move Left   | ⬅️ Left   |
| ✋ Open Palm    | Idle        | —         |


---

## 🛠️ Notes

- Run the script **before** focusing the game window  
- Works best in **well-lit** environments  
- Add your own gestures by modifying `game.py` logic  

---

## 🙋‍♂️ Author

**Maheswaram M V Subrahmanyam**  
📧 [maheswaram.dev@gmail.com](mailto:maheswaram.dev@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/maheswaram-subrahmanyam)  
🌐 [Portfolio](https://maheswaram.me)

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share it.

---

## 📝 To-Do

- [ ] Add gesture customization UI  
- [ ] Support for dual-hand gesture detection  
- [ ] Expand compatibility to other games and emulators


---

### ✅ What You Should Replace (If Not Already):

- Replace `[YOUR_VIDEO_ID](https://youtu.be/tU3b43tUR5Y)` in the demo link with your YouTube video ID.


