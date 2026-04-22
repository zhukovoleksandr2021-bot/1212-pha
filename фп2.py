import cv2
from ultralytics import YOLO

# Завантажуємо модель
model = YOLO('yolov8n.pt')

img_path = '3.jpg'
img = cv2.imread(img_path)

# Шукаємо людей (0) та об'єкти, які модель може прийняти за зброю
# Для стандартної моделі це ніж (43) або телефон (67).
# Якщо у вас є спецмодель, впишіть її класи.
results = model.predict(source=img, classes=[0, 43, 67], conf=0.3)

persons = []
weapons = []

# Розподіляємо об'єкти за списками
for r in results:
    for box in r.boxes:
        cls = int(box.cls)
        coords = box.xyxy.cpu().numpy()[0]
        if cls == 0:
            persons.append(coords)
        else:
            weapons.append(coords)

# Обробка кожної людини
for p in persons:
    px1, py1, px2, py2 = p
    w = px2 - px1
    h = py2 - py1
    center_x = int(px1 + w // 2)
    center_y = int(py1 + h // 2)

    # Перевіряємо, чи є зброя в зоні цієї людини
    has_weapon = False
    for w_box in weapons:
        wx1, wy1, wx2, wy2 = w_box
        # Центр об'єкта зброї
        c_wx, c_wy = (wx1 + wx2) / 2, (wy1 + wy2) / 2

        # Якщо центр зброї всередині прямокутника людини (з невеликим запасом)
        if px1 <= c_wx <= px2 and py1 <= c_wy <= py2:
            has_weapon = True
            break

    # Вибираємо колір: червоний (BGR: 0,0,255) для озброєних, зелений (0,255,0) для інших
    color = (0, 0, 255) if has_weapon else (0, 255, 0)

    # Малюємо приціл (зменшений у 3 рази)
    thickness = 2
    offset_w, offset_h = int(w // 6), int(h // 6)

    cv2.line(img, (center_x - offset_w, center_y), (center_x + offset_w, center_y), color, thickness)
    cv2.line(img, (center_x, center_y - offset_h), (center_x, center_y + offset_h), color, thickness)

cv2.imshow('Security Monitor', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
