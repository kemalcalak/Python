import cv2   

img = cv2.imread("face.png")

# Kullanacağımız cascade dosyasını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("frontalface.xml")

# Haar-like özellikleri kolay algılayabilmek için resmimizi boz(gri) tonlara çevirelim.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Şimdi de cascade dosyamızı kullanarak resim üzerindeki yüzlerin koordinarlarını bulalım.
faces = face_cascade.detectMultiScale(gray, 1.3, 7)

# "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

# İşlediğimiz resmi görelim.
cv2.imshow('image',img)

# Son olarak programı kapatacak kodu yazalım.
cv2.waitKey(0)
cv2.destroyAllWindows()
