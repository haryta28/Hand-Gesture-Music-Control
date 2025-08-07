# Hand-Gesture-Music-Control
Hand Gesture Controlled Music &amp; Volume on MacBook (Python + OpenCV): A computer vision project using Python, OpenCV, and MediaPipe to detect hand gestures via webcam. Specific finger positions and distances were mapped to control music playback (play/pause, next/previous) and adjust system volume.

Hand Gesture Control Projects using Python + OpenCV

This repository contains two computer vision-based projects that utilize hand gestures for controlling media functions—**music playback** and **system volume**—on a MacBook. Both projects are built using Python, OpenCV, and MediaPipe.

🔊 Project 1: Hand Gesture-Based Volume Control

📝 Description
A Python project that allows users to control the system volume using hand gestures captured via webcam. By measuring the distance between the thumb and index finger, the volume level is adjusted in real time—providing a touchless and intuitive user experience.

 ⚙️ Technologies Used
- Python
- OpenCV
- MediaPipe
- Pycaw (for controlling system audio on Windows; macOS alternatives used if applicable)

🎯 Features
- Real-time hand tracking
- Dynamic volume control using thumb–index finger distance
- Visual feedback through volume bars and FPS counter

🚀 How It Works
1. The webcam captures hand movements.
2. MediaPipe detects landmarks of the hand.
3. The distance between the thumb and index finger is calculated.
4. This distance is mapped to a system volume range and updated live.

🎵 Project 2: Hand Gesture Controlled Music Player

📝 Description
A gesture-controlled music player that uses hand gestures to play/pause music, skip tracks, and navigate through a playlist without physical interaction. The webcam tracks hand signs and executes the corresponding media control action.

 ⚙️ Technologies Used
- Python
- OpenCV
- MediaPipe
- OS-specific libraries (e.g., AppleScript or `pyautogui` for Mac)

 🎯 Features
- Play/Pause music using specific hand signs
- Skip to next or previous track with directional gestures
- Cross-platform support (customized for macOS)

 🚀 How It Works
1. The webcam captures your hand movements.
2. MediaPipe identifies the gesture using landmark positions.
3. Each gesture is mapped to a music command (e.g., play, pause, next).
4. Actions are triggered using system-level scripts or automation tools.

📸 Demo

<img width="600" height="375" alt="Image" src="https://github.com/user-attachments/assets/6a59f1ac-8b2f-4e02-aff8-03df3539398b" />

<img width="600" height="375" alt="Image" src="https://github.com/user-attachments/assets/4d0cd0e3-d16f-4549-82e5-723eaf7ecf8f" />

<img width="600" height="375" alt="Image" src="https://github.com/user-attachments/assets/3f5d1e04-50a1-4ac2-8ff5-53a49b5fa350" />

<img width="600" height="375" alt="Image" src="https://github.com/user-attachments/assets/f0a57656-d251-417a-8159-e1bde86d49cf" />

<img width="600" height="700" alt="Image" src="https://github.com/user-attachments/assets/ebf7717b-ba57-4296-8fa2-0b6fe6eb1879" />

<img width="600" height="708" alt="Image" src="https://github.com/user-attachments/assets/562474e0-51a1-4d20-843e-eeccebb77281" />

<img width="600" height="666" alt="Image" src="https://github.com/user-attachments/assets/1e95734a-c9e2-469a-b9b2-6bfabab508a3" />

Prerequisites
- Python 3.7+
- Webcam
- macOS (tested) or Windows (for Pycaw compatibility)

