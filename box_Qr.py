from ultralytics import YOLO
import cv2
import pyttsx3
from pyzbar.pyzbar import decode
import time

# Constants for distance estimation
KNOWN_WIDTH = 15.0  # in cm
FOCAL_LENGTH = 700  # based on calibration

# Load YOLOv8 model
model = YOLO("best.pt")

# Setup text-to-speech
engine = pyttsx3.init()

# Open video
cap = cv2.VideoCapture("box_1.mp4")
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Variables for controlling speech and duplicate QR handling
last_spoken_time = 0
speak_interval = 6 # seconds
last_qr_data = ""
speak_count = 0     # track how many times we've spoken
MAX_SPEAK = 3       #  speak only 3 times total

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        box_width_in_pixels = x2 - x1

        # Distance calculation
        if box_width_in_pixels > 0:
            distance = (KNOWN_WIDTH * FOCAL_LENGTH) / box_width_in_pixels
            distance_text = f"Distance: {int(distance)} cm"
            cv2.putText(annotated_frame, distance_text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            # Read QR code from cropped ROI
            roi = frame[y1:y2, x1:x2]
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            qr_codes = decode(gray)

            for qr in qr_codes:
                qr_data = qr.data.decode('utf-8')
                qr_text = f"QR: {qr_data}"
                cv2.putText(annotated_frame, qr_text, (x1, y2 + 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

                current_time = time.time()
                if speak_count < MAX_SPEAK and ((current_time - last_spoken_time >= speak_interval)):
                    sentence = f"The object is {int(distance)} centimeters away. QR content is: {qr_data}"
                    engine.say(sentence)
                    engine.runAndWait()
                    last_spoken_time = current_time
                    last_qr_data = qr_data
                    speak_count += 1  #  increment the counter

    # Show result
    cv2.imshow("Detection + QR + Distance", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




