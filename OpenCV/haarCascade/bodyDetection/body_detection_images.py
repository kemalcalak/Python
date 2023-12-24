import cv2   

img = cv2.imread("...")

body_cascade = cv2.CascadeClassifier("...")

#  Haar-like özellikleri kolay algılayabilmek için resmi boz(gri) tonlara çevirelim.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#  Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
bodies = body_cascade.detectMultiScale(gray,1.1,5)

#  "bodies" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
         
#  İşlediğimiz kareleri görelim.
cv2.imshow('image',img)

#  Son olarak videoyu serbest bırakalım.
cv2.waitKey(0)
cv2.destroyAllWindows()
