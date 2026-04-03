import cv2

cat_img_path = '234.jpg'

cat_fase_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface_extended.xml')

img = cv2.imread(cat_img_path)

cat_fase = cat_fase_cascade.detectMultiScale(img)

print(cat_fase)

for (x,y,w,h) in cat_fase:
    cv2.rectangle(img,(x,y),(x+w, y+h),(159,128,255), 3)

cv2.imshow('Cat', img)
cv2.waitKey()