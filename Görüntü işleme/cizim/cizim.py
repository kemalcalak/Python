import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

# Çizgi çizme
cv2.line(canvas, (50, 50), (512, 512)(255, 0, 0), thickness=5)
cv2.line(canvas, (100, 50), (200, 250)(0, 0, 255), thickness=7)

# Dikdörtgen çizme
cv2.rectangle(canvas, (20, 20), (50, 50)(0, 255, 0), thickness=-1)
cv2.rectangle(canvas, (50, 50), (150, 150)(0, 255, 0), thickness=-1)

# Çember çizme
cv2.circle(canvas, (250, 250), 100, (0, 0, 255), thickness=5)

# Daire çizme
cv2.circle(canvas, (250, 250), 100, (0, 0, 255), thickness=-1)

# Üçgen çizme
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

cv2.line(canvas, p1, p2, (0, 0, 0), thickness=4)
cv2.line(canvas, p2, p3, (0, 0, 0), thickness=4)
cv2.line(canvas, p1, p3, (0, 0, 0), thickness=4)

# Çokgen çizme
pts = np.array([[10, 50], [400, 50], [90, 200], [50, 500]], np.int32)
cv2.polylines(canvas, [pts], True, (0, 255, 255), thickness=5)

# Elips çizme
cv2.ellipse(canvas, (256, 256), (100, 50), 10, 90, 360, (255, 0, 0), thickness=5)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
