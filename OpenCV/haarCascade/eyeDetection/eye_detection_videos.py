import cv2

# VideoCapture object
vid = cv2.VideoCapture("...")

# Load the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier("...")
eye_cascade = cv2.CascadeClassifier("...")

while True:
    # Read a frame from the video
    ret, frame = vid.read()

    # Resize the frame
    frame = cv2.resize(frame, (480, 360))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Iterate over detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract the region of interest (ROI) for eyes within the face rectangle
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes in the ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Iterate over detected eyes and draw rectangles
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
vid.release()
cv2.destroyAllWindows()
