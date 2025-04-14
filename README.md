---
title: "🖐️ Gesture Controlled Game Bot 🎮"
description: "Control games with your hand gestures using Python, OpenCV, and MediaPipe."
author: "Maheswaram M V Subrahmanyam"
email: "youremail@example.com"
linkedin: "https://www.linkedin.com/in/your-profile"
portfolio: "https://yourportfolio.com"
license: "MIT"
---

# 🖐️ Gesture Controlled Game Bot 🎮

Control your favorite games using simple hand gestures via webcam!  
This project uses **MediaPipe**, **OpenCV**, and **PyAutoGUI** to detect hand gestures and simulate keyboard inputs — tested with **Subway Surfers on Poki.com**.

## 📽️ Demo
> *(Add a demo GIF or YouTube video link here)*

## ✨ Features
- Real-time hand tracking with MediaPipe
- Game controls using intuitive gestures
- Simple and lightweight implementation
- Cooldown system to prevent multiple triggers

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/gesture-game-bot.git
cd gesture-game-bot
Dependencies
bash
Copy
Edit
pip install opencv-python mediapipe pyautogui
✅ Make sure you have Python 3.7+ installed

▶️ Run the Project
bash
Copy
Edit
python gesture_controller.py
⚠️ IMPORTANT: Keep your game window (e.g., Subway Surfers in browser) focused after launching the script.

🧠 How It Works
yaml
Copy
Edit
- Uses webcam to track hand landmarks (MediaPipe)
- Detects specific finger positions to classify gestures
- Triggers key presses using PyAutoGUI
🧪 Supported Gestures
Gesture	Action	Key Press
✊ Fist	Slide	⬇️ Down
☝️ Index Only	Jump	⬆️ Up
✌️ Peace Sign	Move Right	➡️ Right
👌 OK Sign	Move Left	⬅️ Left
✋ Open Palm	Idle	—
🛠️ Notes
yaml
Copy
Edit
- Run the script and immediately focus the game window
- Works best in well-lit conditions
- You can add or modify gestures by tweaking the code logic
🙋‍♂️ Author
yaml
Copy
Edit
name: Maheswaram M V Subrahmanyam
email: youremail@example.com
linkedin: https://www.linkedin.com/in/your-profile
portfolio: https://yourportfolio.com
📄 License
This project is licensed under the MIT License.

📝 To-Do
yaml
Copy
Edit
- Add gesture customization
- Add support for two-handed gesture detection
- Integrate with more games and platforms
yaml
Copy
Edit

---

### ✅ Before Publishing:
- Replace all placeholders like `<your-username>`, `youremail@example.com`, and links with your real info.
- Add a video or GIF demo for better engagement.

Want a custom GitHub banner for this project? I can generate a modern one with your name and title — just say 