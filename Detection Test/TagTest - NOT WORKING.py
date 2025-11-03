import cv2
from dt_apriltags import Detector

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create detector (tag36h11 family is most common)
detector = Detector(families='tag36h11')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale (AprilTag detector works on grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect tags
    results = detector.detect(gray)

    for r in results:
        # Each detection has corners: [top-left, top-right, bottom-right, bottom-left]
        corners = r.corners.astype(int)

        # Draw polygon around the tag
        cv2.polylines(frame, [corners], isClosed=True, color=(0, 255, 0), thickness=2)

        # Draw tag ID at the center
        cX, cY = r.center.astype(int)
        cv2.putText(frame, str(r.tag_id), (cX - 10, cY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # Print ID and pose info
        print(f"Detected tag ID: {r.tag_id}")

    # Show frame
    cv2.imshow("AprilTag Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
