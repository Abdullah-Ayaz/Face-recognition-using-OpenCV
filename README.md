
# Face Recognition via OpenCV

This project utilizes the `face_recognition` library along with `OpenCV` to perform real-time face recognition and measure the distance between the camera and the detected faces. The system is designed to identify known faces and display their names, along with the estimated distance from the camera.

## Overview

The project captures live video using the computer's camera, processes each frame to detect faces, and then compares them to pre-encoded known faces. For each recognized face, the program displays the name and computes the approximate distance from the camera based on the size of the face.

### Key Features

- **Real-time Face Detection**: Detects faces in real-time video frames.
- **Face Recognition**: Compares the detected faces to known faces stored in memory and displays the name of the recognized individual.
- **Distance Measurement**: Estimates the distance between the camera and the detected face using a simple mathematical formula.
- **Bounding Box & Centroid**: Draws bounding boxes around detected faces and marks the center of the face with a circle.

## Dependencies

To run this project, you need the following Python libraries:

- `face_recognition` - For encoding faces and comparing them.
- `opencv-python` - For video capture and image processing.
- `numpy` - For handling numerical operations.

You can install these dependencies using `pip`:

```bash
pip install face_recognition opencv-python numpy
