import easyocr
import cv2

cap = cv2.imread('abc1.jpg')
reader = easyocr.Reader(['en'], gpu=False)

def read_license_plate(license_plate_crop):
    detections = reader.readtext(license_plate_crop)

    for detection in detections:
        bbox, text, score = detection

        text = text.upper().replace(' ', '')
    return text, score

text, _ = read_license_plate(cap)

print(text)
print(_)
cv2.imshow('ab',cap)
cv2.waitKey(0)