import cv2
from ultralytics import YOLO

# 1. Load your model
model = YOLO('best.pt')

# 2. Open Webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Run YOLO inference on the frame
    # stream=True is efficient for videos
    results = model(frame, stream=True, conf=0.5)

    # 4. Plot results directly on the frame
    for result in results:
        annotated_frame = result.plot()

    # 5. Display the frame
    cv2.imshow("Weapon Detection (Local)", annotated_frame)

    # Quit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()