import sqlite3

DB_PATH = "data/plate_db.sqlite"

def create_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS plates (plate TEXT PRIMARY KEY)")
    conn.commit()
    conn.close()

def is_plate_in_db(plate_text):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT 1 FROM plates WHERE REPLACE(plate, ' ', '') = ?", (plate_text.replace(" ", ""),))
    result = c.fetchone()
    conn.close()
    return result is not None

def insert_plate(plate_text):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO plates (plate) VALUES (?)", (plate_text,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()
