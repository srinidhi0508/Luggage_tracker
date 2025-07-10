# Luggage_tracker 
A smart luggage tracking system for visually impaired individuals. The system detects luggage using YOLOv11, reads QR codes attached to the luggage to identify contents, estimates the distance from the user, and provides real-time audio feedback.
# 🎒 Smart Luggage Tracking System for the Visually Impaired

## 🧠 Features

- 🎯 **Object Detection**: Uses YOLOv11 to detect luggage in real-time video.
- 📏 **Distance Estimation**: Calculates the distance from the user to the detected luggage using bounding box width.
- 🔍 **QR Code Reading**: Scans a QR code attached to the luggage to identify its contents.
- 🔊 **Voice Feedback**: Narrates the luggage distance and QR content using text-to-speech (TTS) output.
- 🚫 **Limited Voice Output**: Only speaks up to 3 times to avoid overwhelming the user.

---

## 🔧 Tech Stack

- Python
- [YOLOv11](https://github.com/ultralytics/ultralytics)
- OpenCV
- pyttsx3 (TTS)
- pyzbar (QR code scanner)

## 📂 Project Structure
smart-luggage-tracker/
- best.pt # Trained YOLOv11 model
- sample_video.mp4 # output demo
- box_Qr.py # Main detection and voiceover script
- requirements.txt # Python dependencies
- README.md # Project overview

## Outputs
<img width="554" height="549" alt="Screenshot 2025-06-24 162523" src="https://github.com/user-attachments/assets/5a8b296e-1bf2-40eb-9fa9-bf297d747efc" />

## Author
  - created by Srinidhi Vodnala

