from ultralytics import YOLO
import cv2

model = YOLO("best.pt")
img = cv2.imread("luggage.jpg")
results = model(img)[0]
annotated = results.plot()

cv2.imshow("Luggage Detection", annotated)
cv2.imwrite("photo_output.jpg", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

