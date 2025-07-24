import cv2
import time

# Load Haar cascade for face detection
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Open webcam (0 = default)
cap = cv2.VideoCapture(0)

# Counter for saved images
img_counter = 0

while True:
    # Read frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

    if len(faces) > 0:
        # Draw rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Save frame with rectangles — only once per detection cycle
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        img_name = f"captured_face_{timestamp}_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f"✅ Saved: {img_name}")
        img_counter += 1

        # Optional: Wait to avoid saving multiple times per second
        time.sleep(1)

    # Show video
    cv2.imshow('Face Detector', frame)

    # Break with ESC
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
