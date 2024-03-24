# Rubik's Cube Move Detection

This project aims to develop a system for recognizing hand gestures and detecting Rubik's Cube faces independently, with the intention of merging both functionalities to detect cube rotations based on hand movements.

## Detecting Rubik's Cube Faces
The Rubik's Cube face detection consists of files: `detect.py` and `functions.py`.

### detect.py
The `detect.py` script is the main detection module responsible for detecting the faces of a Rubik's Cube using computer vision techniques. It performs the following tasks:

- Captures video feed from the webcam.
- Applies image processing techniques such as contour detection and color analysis to identify the faces of the Rubik's Cube.
- Determines the colors of each face.
- Outputs the detected Rubik's Cube faces.

### functions.py
The `functions.py` file contains all the functions used in the Rubik's Cube face detection process. These functions include:

- Drawing contours and annotations on the detected Rubik's Cube faces.
- Extracting dominant colors from the detected faces.

## Hand Gesture Recognition
The hand gesture recognition module consists of the `hand_gesture.py` file.

### hand_gesture.py
The `hand_gesture.py` script utilizes the MediaPipe library for detecting hand landmarks and recognizing gestures. It performs the following tasks:

- Captures video feed from the webcam.
- Uses the MediaPipe Hands model to detect hand landmarks in the video frames.
- Analyzes the movement of fingers and hand positions to recognize specific gestures.
- Outputs the recognized hand gestures.

## Requirements
To run the Rubik's Cube gesture recognition system, you need the following dependencies:

- Python 3.x
- OpenCV (cv2)
- MediaPipe
- NumPy
- pyciede2000 (for color comparison)

You can install the required dependencies using `pip`:
```
pip install opencv-python mediapipe numpy pyciede2000
```

## Future Steps
Currently, the Rubik's Cube face detection and hand gesture recognition functionalities are being developed independently. Once both modules provide accurate results individually, we will proceed to merge them to detect cube rotations based on hand movements. The merged system will:

- Detect changes in Rubik's Cube colors using the face detection module.
- Track hand movements and gestures using the hand gesture recognition module.
- Analyze the intersection of hand positions and Rubik's Cube faces to determine cube rotations.
- Output the detected cube rotations in real-time.

Stay tuned for updates as we progress with the development and integration of these functionalities.

