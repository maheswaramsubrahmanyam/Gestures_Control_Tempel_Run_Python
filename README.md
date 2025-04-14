# 🖐️ Gesture Controlled Game  🎮

Control your favorite games with just your hand gestures using **Python**, **OpenCV**, and **MediaPipe**.  
This bot simulates keyboard inputs based on real-time hand tracking and works seamlessly with browser games like **Tempel run, Subway Surfers on Poki.com**.

---

## 📽️ Demo

[![Watch the demo](https://github.com/user-attachments/assets/0b3b674f-815b-47b7-8182-44116299f8fe)] 

---
[![demo] (https://youtu.be/tU3b43tUR5Y))]

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
git clone https://github.com/maheswaramsubrahmanyam/Gestures_Control_Tempel_Run_Python.git


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
📧 [msdevgoog01@gmail.com](mailto:msdevgoog01@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/maheswaram-subrahmanyam-361238275/)  
🌐 [Portfolio](https://maheswaramsubrahmanyam.github.io/Maheswaram-Subrahmanyam-Potfolio-website/)

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
