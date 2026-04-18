 🚀 ASIS - Adaptive Screen Interaction System

🧠 Overview

ASIS (Adaptive Screen Interaction System) is an AI-powered multimodal human-computer interaction system that enables users to control a computer using **hand gestures, voice commands, and facial interaction**, eliminating the need for traditional input devices like a mouse or keyboard.

🎯 Features

 👋 Gesture Control

* Cursor movement
* Left / Right / Double click
* Scroll up / down
* Drag and drop
* Zoom in / out
* Screenshot capture
* Volume control
* Tab switching

🎤 Voice Assistant (Jarvis)

* Wake word activation ("Jarvis")
* Commands:

  * Click
  * Scroll
  * Open applications (e.g., Chrome, Notepad)
* Fallback to text input if microphone fails

👤 Face Login

* Camera-based login system
* Secure entry before system activation

 📊 Analytics & Database

* Logs all gestures
* Tracks usage patterns
* Displays analytics charts

🤖 Auto Training

* Continuously improves model using collected data

🖥️ Dashboard UI

* Modern dark-themed interface
* Start/Stop system
* Logs panel
* Analytics button

---

🏗️ System Architecture

```text
Camera / Microphone Input
        ↓
Computer Vision + Speech Recognition
        ↓
Machine Learning Model (KNN)
        ↓
Action Mapping Engine
        ↓
OS Control (Mouse / Keyboard)
```

---

🧰 Tech Stack

| Category          | Technology        |
| ----------------- | ----------------- |
| Language          | Python            |
| Computer Vision   | OpenCV, MediaPipe |
| Machine Learning  | KNN               |
| Voice Recognition | SpeechRecognition |
| UI                | CustomTkinter     |
| Automation        | PyAutoGUI         |
| Database          | SQLite            |
| Visualization     | Matplotlib        |

---

⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/ASIS-AI-System.git
cd ASIS-AI-System
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

---

▶️ Usage

 Step 1: Train the model

```bash
python train_model.py
```

Step 2: Run the system

```bash
python dashboard.py
```

---

🎮 Supported Gestures

* Move
* Click
* Right Click
* Double Click
* Scroll Up / Down
* Drag
* Zoom In / Out
* Screenshot
* Volume Control
* Tab Navigation

---

🗣️ Voice Commands

* "Jarvis" → Activate system
* "Click" → Perform click
* "Scroll up/down"
* "Open Chrome"
* "Open Notepad"

---

📊 Analytics

* Gesture usage tracking
* Real-time logs
* Visual charts

---

🚀 Future Scope

* Deep learning-based gesture recognition
* Mobile app integration
* Cloud-based analytics
* Face recognition authentication

---

🎯 Problem Statement

Traditional input devices limit accessibility and flexibility.

---

💡 Solution

ASIS provides a **touchless, AI-driven interaction system** for natural and efficient computer control.

---

🏁 Conclusion

ASIS demonstrates the future of human-computer interaction through AI, combining gesture, voice, and vision into a unified system.

---

👨‍💻 Author

**Ram**

---

⭐ If you like this project, give it a star!
