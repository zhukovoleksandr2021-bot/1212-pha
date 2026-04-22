import cv2

img_path = '234.jpg'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    thickness = 2
    red_color = (0, 0, 255)

    # Знаходимо центр
    center_x = x + w // 2
    center_y = y + h // 2

    # Розраховуємо довжину ліній (1/3 від розміру обличчя)
    # Тобто від центру відступаємо на 1/6 частину в кожен бік
    offset_w = w // 6
    offset_h = h // 6

    # Малюємо зменшену горизонтальну лінію
    cv2.line(img, (center_x - offset_w, center_y), (center_x + offset_w, center_y), red_color, thickness)

    # Малюємо зменшену вертикальну лінію
    cv2.line(img, (center_x, center_y - offset_h), (center_x, center_y + offset_h), red_color, thickness)

cv2.imshow('Small Target', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

