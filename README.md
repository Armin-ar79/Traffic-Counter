# 🚗 AI Traffic Counter & Tracker

An intelligent computer vision system that detects, tracks, and counts vehicles (Cars, Trucks, Buses) in real-time using **YOLOv8** and **OpenCV**.

## 📝 Description

This project processes video footage to monitor traffic flow. Unlike simple object detectors, it uses a tracking algorithm to assign unique IDs to vehicles. This allows the system to accurately count vehicles only when they cross a specific line, distinguishing between different vehicle types.

## ✨ Features

- **Real-time Detection:** Uses the state-of-the-art YOLOv8 Nano model for fast performance.
- **Object Tracking:** Robust tracking to handle moving vehicles and occlusions.
- **Class Classification:** Separately counts:
  - 🚗 Cars
  - 🚛 Trucks
  - 🚌 Buses
- **Counting Logic:** Increments count only when the center of the vehicle crosses a defined line.
- **Video Export:** Automatically saves the processed video with overlays to your disk.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Computer Vision:** OpenCV (`cv2`)
- **AI Model:** Ultralytics YOLOv8 (`yolov8n`)

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone (https://github.com/Armin-ar79/Traffic-Counter.git)

2. **Install dependencies:**
    pip install ultralytics opencv-python
3. **Run the script:**
   Ensure you have a video file (e.g., traffic.mp4) in the directory and update the video_path in the code if necessary.

python counter.py

📂 Project Structure
├── counter.py          # Main application script
├── traffic.mp4         # Input video file (sample)
├── output_final.mp4    # Processed output video
└── README.md           # Project documentation

Developed with ❤️ by Armin
