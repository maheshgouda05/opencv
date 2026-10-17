
import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Open the webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Face Detection Started")
print("Press 'q' to quit.")

while True:
    # Capture a frame
    success, frame = camera.read()

    if not success:
        print("Error: Could not read the camera.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Face Detected",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    # Display the number of faces
    cv2.putText(
        frame,
        f"Faces: {len(faces)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    # Show the camera output
    cv2.imshow("Real-Time Face Detection", frame)

    # Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
camera.release()
cv2.destroyAllWindows()
