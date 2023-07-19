import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

# Metin yazma
cv2.putText(
    canvas,
    "Ali Kemal Calak",
    (10, 100),
    font1,
    2,
    (0, 0, 0),
    thickness=5,
)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
