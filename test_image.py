import argparse
import cv2
from app.ocr_reader import detect_plate_text

parser = argparse.ArgumentParser()
parser.add_argument("--image", required=True, help="Path to test image")
args = parser.parse_args()

img = cv2.imread(args.image)
texts = detect_plate_text(img)

print("📋 OCR Results:")
for t in texts:
    print(f"→ {t}")
