# ✈️ Smart Assistive Luggage Detection and Tracking System

This project is a Computer Vision-based Smart Assistive System designed to **detect and track airport luggage** from video footage using a custom-trained **YOLOv8** model and the **DeepSORT** tracking algorithm.

It simulates how intelligent systems can assist in **airport baggage management**, surveillance, and automation.


## 🚀 Features

- 🎯 Real-time luggage detection using YOLOv8
- 🧠 Object tracking with DeepSORT (assigns consistent IDs to each luggage)
- 📹 Supports video input (e.g. CCTV footage, recorded mp4 files)
- 💾 Outputs annotated video with tracking info
- 🔩 Easily extendable for edge devices or real-time use

---

## 🧰 Tech Stack

- Python 3.x
- [YOLOv11 (Ultralytics)]([https://github.com/ultralytics/ultralytics])
- OpenCV
- DeepSORT (via `deep_sort_realtime`)
- PyTorch

---

📁 project_root/
-  best.pt 
- luggage_clip.mp4 
- track_luggage.py 
- racked_output.mp4 


🧠 How It Works
- YOLOv8 detects luggage objects in each frame.
- DeepSORT keeps track of each detected luggage across frames and assigns it a unique, consistent ID.
- OpenCV handles video input/output and visualizations.

📍 Use Cases
- Airport luggage tracking and management
- Surveillance automation
- Assistive tools for lost luggage detection
- Smart carts or autonomous luggage systems

  🧑‍💻 Author
  srinidhi vodnala
Computer Vision & AI Developer
