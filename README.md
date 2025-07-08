# ⚽ Football Broadcast Player Detection & Re-Identification using YOLOv11

This repository presents a system for detecting and re-identifying players in football match broadcasts. The model is custom-trained on an annotated dataset using YOLOv11 and includes a tracking pipeline for player association across video frames.

---
## 📂 Project Overview

This project enables:
- ⚡ Real-time detection of players, referee, football, and objects
- 🏷️ Re-identification of players across frames using tracking
- 🎥 Generation of output videos with bounding boxes and identities
- 📁 Saving detection and tracking results as `.pkl` files

---

📦 Directory Structure
```
.
├── input_video/               # Source input video
├── model/                     # Model export or download link
├── output_videos/sf/          # Output results
├── tracker_stubs/             # .pkl file for tracking results
├── trackers/                  # Custom tracker logic
├── utils/                     # Utility functions
├── yolo_inference.py          # YOLO detection logic
├── main.py                    # Entry point script
├── requirements.txt           # Python dependencies
└── README.md                  # You are here
```
## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/UtkarshTrivedi2934/Assignment-Player-Re-Identification-in-Sports-Footage.git
cd Assignment-Player-Re-Identification-in-Sports-Footage
```
### 2️⃣ Create and Activate Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows

venv\Scripts\activate

# On Unix/macOS
source venv/bin/activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
**⚠️ Known Issue During requirements.txt Installation**
If you encounter the following error while installing dependencies:
```bash
Could not find a version that satisfies the requirement torch>=1.7.0 (from ultralytics->-r requirements.txt)
No matching distribution found for torch>=1.7.0
```
*✅ Fix: Ensure the following conditions are met before running pip install -r requirements.txt:*

- You are using Python 3.8 to 3.11 (preferably 64-bit)
- You have updated pip to the latest version

**Or install manually:**
```bash
pip install opencv-python torch torchvision numpy pillow scikit-learn ultralytics
```

### ▶️ Running the Code

**Tracking and Player Re-Identification**

```bash
After replacing with your trained model:
model = YOLO("model/best.pt")  # fine-tuned YOLOv11 model
results = model.track(source="input_video/15sec_input_720p.mp4", save=True, persist=True)

```
- Annotated video with player IDs: runs/track/predict/
- Frame-wise results or Re-ID metadata: tracker_stubs/player_detection.pkl
---

**📌 Output:**

- Players and referees are marked with consistent Re-ID numbers (as shown in the output image).
- Objects such as the football are accurately detected and tracked.
- Frame-by-frame tracking metadata is saved in tracker_stubs/player_detection.pkl.

### 🧾 Dependencies
- Python 3.8+
- OpenCV
- Ultralytics
- Torch + TorchVision
- Torchreid
- scikit-learn
- Pillow

---
