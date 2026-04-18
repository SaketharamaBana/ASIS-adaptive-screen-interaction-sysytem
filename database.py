import sqlite3, time

def connect():
    return sqlite3.connect("gestures.db")

def init_db():
    conn = connect()
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS logs (time TEXT, msg TEXT)")
    conn.commit()
    conn.close()

def log_event(msg):
    conn = connect()
    c = conn.cursor()

    c.execute("INSERT INTO logs VALUES (?, ?)",
              (time.strftime("%H:%M:%S"), msg))

    conn.commit()
    conn.close()

def get_logs():
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT * FROM logs ORDER BY time DESC LIMIT 20")
    data = c.fetchall()

    conn.close()
    return data