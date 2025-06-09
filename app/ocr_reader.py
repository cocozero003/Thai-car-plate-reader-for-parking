import easyocr
import cv2

reader = easyocr.Reader(['th', 'en'])

def detect_plate_text(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    roi = gray[int(h * 0.5):h, int(w * 0.25):int(w * 0.75)]
    results = reader.readtext(roi)
    return [text for (_, text, conf) in results if conf > 0.5]
