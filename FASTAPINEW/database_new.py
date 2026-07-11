import sqlite3


def send_to_sql(data):

    conn = sqlite3.connect("emails_new.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipient TEXT,
        subject TEXT,
        message TEXT,
        date TEXT,
        time TEXT, 
        status TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO emails(recipient, subject, message, date, time, status)
    VALUES(?,?,?,?,?,?)
    """,
    (
    data.recipient,
    data.subject,
    data.message,
    data.date.strftime("%d-%m-%Y"),
    data.time.strftime("%H:%M"),
    "Pending"
))

    conn.commit()

    conn.close()


def get_pending_emails():

    conn = sqlite3.connect("emails_new.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM emails
    WHERE status='Pending'
    """)

    emails = cursor.fetchall()
    print("Pending Emails:", emails)
    conn.close()

    return emails


def update_status(email_id):

    conn = sqlite3.connect("emails_new.db")

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE emails
    SET status='Sent'
    WHERE id=?
    """, (email_id,))

    conn.commit()
    print(f"Email {email_id} marked as Sent")
    print("Email stored successfully in SQLite")

    conn.close()