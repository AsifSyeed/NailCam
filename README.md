
# NailCam

**AI-powered habit tracker that detects nail biting through webcam and alerts you in real time.**

---

## 🧠 The Problem

As a software engineer, I often bit my nails during deep focus without realizing it. I needed a simple, private solution to help me become aware of the habit and stop it.

---

## 💡 The Solution

**NailCam** is a lightweight macOS app that uses your webcam and AI-powered gesture detection to identify when your hand is near your mouth — a common nail-biting gesture. It alerts you with:

- 🔔 A native macOS notification  
- 🔊 A subtle sound (like a ping)

This immediate feedback helps build awareness and break the habit over time.

---

## 🎯 Features

- 🧠 Detects hand-to-mouth gestures in real time using [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/guide)
- 🔔 Sends a macOS notification
- 🔊 Plays a system sound when a bite gesture is detected
- 📷 100% local processing — your webcam feed never leaves your machine
- 🛠 Built entirely with Python

---

## 🛠 Setup

### Requirements

- macOS (Intel tested)
- Python 3.10
- Conda (recommended)
- Webcam

### Installation

```bash
# Create and activate environment
conda create -n nailcam python=3.10
conda activate nailcam

# Install dependencies
pip install opencv-python mediapipe pyobjc
```

---

## ▶️ Run It

```bash
python nailcam.py
```

Once running, NailCam opens your webcam and silently monitors for nail-biting gestures. When detected, it alerts you with a notification and a system sound.

---

## 🔧 Customization

### Change the System Sound

In `nailcam.py`, update:

```python
os.system("afplay /System/Library/Sounds/Ping.aiff")
```

You can replace `"Ping.aiff"` with:

- `Glass.aiff`
- `Submarine.aiff`
- `Funk.aiff`
- `Basso.aiff`
- `Pop.aiff`

### Adjust Detection Sensitivity

```python
if distance < 0.07:  # Lower means more sensitive
```

---

## 🔐 Privacy Focus

NailCam does **not** record, upload, or store any footage. All AI runs locally using your Mac’s CPU and webcam feed.

---

## 👨‍💻 Author

Built by [Asif Syeed](https://github.com/AsifSyeed) — writing code to solve personal problems and help others do the same.

---

## 📄 License

MIT License
