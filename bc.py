import easyocr
import cv2


# cap = cv2.imread('abc1.jpg')
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext('/abc.jpg', detail = 0)
print(result)
