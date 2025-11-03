import cv2
import time
import os

# Parameters
save_dir = "dataset_images"
capture_interval = 0.5  # seconds
duration = 5            # seconds
preview_time = 3        # seconds before capture starts
camera_index = 0        # change if you have multiple webcams

# Create save directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(camera_index)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print(f"Preview for {preview_time} seconds... Position your cube!")

# --- Preview phase ---
start_preview = time.time()
while time.time() - start_preview < preview_time:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
    cv2.imshow("Webcam Preview", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        exit()

print("Starting capture...")

# --- Capture phase ---
start_time = time.time()
img_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    cv2.imshow("Webcam Feed", frame)

    elapsed = time.time() - start_time
    if elapsed >= img_count * capture_interval and elapsed <= duration:
        filename = os.path.join(save_dir, f"img_{img_count:03d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        img_count += 1

    if elapsed > duration:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Finished capturing {img_count} images in {save_dir}")
