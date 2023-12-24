import cv2   

img = cv2.imread("...")

face_cascade = cv2.CascadeClassifier("...")
eye_cascade = cv2.CascadeClassifier("...")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Iterate over detected faces
for (x, y, w, h) in faces:
    # Draw a rectangle around the face
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Extract the region of interest (ROI) for eyes within the face rectangle
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # Detect eyes in the ROI
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # Iterate over detected eyes and draw rectangles
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

# Display the resulting image
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
