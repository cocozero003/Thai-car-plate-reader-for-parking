from app.camera import get_frame
from app.ocr_reader import detect_plate_text
from app.barrier_control import open_barrier
from app.db import is_plate_in_db, create_db

import time

create_db()
last_trigger = ""

frame_skip = 3
frame_count = 0

while True:
    frame = get_frame()
    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    texts = detect_plate_text(frame)
    for text in texts:
        print(f"[OCR] → {text}")
        if text != last_trigger and is_plate_in_db(text):
            open_barrier()
            last_trigger = text
            time.sleep(5)
