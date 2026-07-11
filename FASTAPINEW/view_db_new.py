import sqlite3

def get_allemails():
    conn = sqlite3.connect("emails_new.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emails")
    rows = cursor.fetchall()

    conn.close()
    return rows