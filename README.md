# Thai License Plate Barrier Reader 🛑🚗

A Python-based project to detect and read Thai license plates using OCR and control a parking barrier based on a whitelist.

## Features

- Real-time webcam/IP camera feed
- Thai OCR using EasyOCR
- SQLite-based whitelist
- Simulated parking barrier control
- Modular and optimized for speed

## Setup

```bash
pip install -r requirements.txt
```

## Run the System

```bash
python main.py
```

## Test with Image

```bash
python test_image.py --image static/images/car1.jpg
```

## Initialize Plate Database

```bash
python init_db.py
```

## License

MIT License
