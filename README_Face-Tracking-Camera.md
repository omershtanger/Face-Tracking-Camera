# Real-Time Face Tracking Camera

A camera that follows a face in real time. A Python program uses OpenCV to detect a face in the video feed and sends movement commands over a serial connection (PySerial) to a servo-mounted camera, which keeps the face centered in the frame.

<!-- Add a demo GIF here, e.g. ![Demo](images/demo.gif) -->

## Features

- **Real-time face detection** with OpenCV
- **Closed-loop tracking:** the camera moves to keep the face centered
- **Serial communication:** PySerial sends control commands from the computer to the microcontroller
- **Servo-actuated mount** for pan (and tilt) motion

## System Overview

```
Camera ──► Python + OpenCV ──► face position ──► PySerial ──► Arduino ──► Servo(s)
   ▲                                                                        │
   └──────────────────────────── camera moves ◄────────────────────────────┘
```

1. A video frame is captured from the camera.
2. OpenCV detects the face and finds its center.
3. The program computes how far the face is from the center of the frame.
4. A command is sent over serial to move the servo in the right direction.
5. The microcontroller moves the servo, and the camera follows the face.

## Hardware

- USB / web camera
- Arduino microcontroller
- Servo motor(s) with a camera mount
- USB cable (serial connection)

## Software Requirements

- Python 3
- OpenCV
- PySerial
- Arduino IDE

```bash
pip install opencv-python pyserial
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/omershtanger/Face-Tracking-Camera.git
   ```
2. Upload the Arduino sketch to the board.
3. Set the correct serial port in the Python script (for example, `COM3` on Windows or `/dev/ttyUSB0` on Linux).
4. Run the Python script and look at the camera.

## Author

**Omer Shtanger**, Electrical Engineering student at Tel Aviv University
[LinkedIn](https://linkedin.com/in/omer-shtanger) · [GitHub](https://github.com/omershtanger)
