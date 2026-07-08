# Real-Time Distance Estimation using YOLO

I built this project because I wanted to answer a simple question can a regular laptop webcam tell you how far away something is? Turns out, yes it can.

This system uses your webcam to detect objects in real time and estimates how far each one is from the camera. No special hardware, no depth sensors, just a webcam and math.

---

## What it does

Point your webcam at anything and the system will:
- Draw a box around every object it detects
- Show the object's name and confidence score
- Calculate and display the distance from the camera in meters
- Color code the box based on how close the object is
  - 🔴 Red — very close (under 1 meter)
  - 🟠 Orange — medium distance (1 to 2 meters)
  - 🟢 Green — far away (beyond 2 meters)

---

## How the distance calculation works

This was the most interesting part to figure out. I used a technique called **focal length estimation** based on this formula:

---

## How to run it

**1. Clone the repo**
```bash
git clone https://github.com/shakk-thii/Real-Time-Distance-Estimation-using-YOLO.git
cd Real-Time-Distance-Estimation-using-YOLO
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run**
```bash
python main.py
```

The YOLOv8 model downloads automatically on first run (~6MB). Press **Q** to quit.

---

## What I learned

Going into this I understood the theory of object detection but hadn't built anything that ran in real time before. The challenging part wasn't the detection itself YOLOv8 handles that well it was figuring out the distance estimation from a single monocular camera without any depth sensor.

The focal length approach has limitations. It assumes objects are facing the camera directly and relies on average known widths which vary in real life. A person standing sideways will appear narrower than 50cm, which throws off the estimate. Improving this with stereo vision or a depth camera like Intel RealSense would give much more accurate results — that's the natural next step for this project.

---

## Author

**S. Shakthikumar**  
Final year B.E. — Computer Science & Engineering  
Specialization: AI & Machine Learning  
shakthikumar2505@gmail.com