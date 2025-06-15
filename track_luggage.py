import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load trained model
model = YOLO("best.pt")

# Initialize DeepSORT tracker
tracker = DeepSort(max_age=30)

# Load video
cap = cv2.VideoCapture("luggage_clip.mp4")

# Output video
out = cv2.VideoWriter("tracked_output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 
                      int(cap.get(cv2.CAP_PROP_FPS)),
                      (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv11 detection
    results = model(frame)[0]
    detections = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        detections.append(([x1, y1, x2 - x1, y2 - y1], conf, cls_id))

    # Update tracker
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, w, h = map(int, track.to_ltrb())
        cv2.rectangle(frame, (l, t), (l + w, t + h), (0, 255, 0), 2)
        cv2.putText(frame, f"Luggage ID {track_id}", (l, t - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
