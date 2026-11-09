# OpenCV Invisibility Cloak

A real-time computer vision project that makes a green object appear invisible by replacing its pixels with a previously captured background.

## Skills demonstrated
Python, OpenCV, NumPy, HSV color segmentation, binary masks, morphological operations, webcam video processing.

## Run
```bash
python -m pip install -r requirements.txt
python invisibility_cloak.py
```

Allow webcam access. Press **b** to capture an empty background, introduce a green object, and press **q** to quit. Use a steady camera and consistent lighting.

## Privacy
Webcam frames are processed locally; this script does not upload or save camera footage.
