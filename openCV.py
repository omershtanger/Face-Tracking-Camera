import cv2
import serial
import time

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start camera
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around faces
    if len(faces)>0:
        (x, y, w, h) = faces[0]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(x-220)
        arduino.write(f"{x-220}\n".encode())

    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        print(f"Arduino says: {line}")


    # Show the result
    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()