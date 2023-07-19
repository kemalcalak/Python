import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # video açma

filename="C:\Kodlar\python\Görüntü işleme\en.avi"
codec = cv2.VideoWriter_fourcc("W", "M", "V", "2")
framerate = 30
resolution = (640, 480)
videoFileOutput=cv2.VideoWriter("filename",codec,framerate, resolution)
while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.flip(frame, 1)
    videoFileOutput.write(frame)

    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()