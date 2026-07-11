import sqlite3

def get_sent_emails():
    conn = sqlite3.connect("emails_new.db")

    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM emails
                WHERE STATUS = 'Sent'
    """)

    emails = cursor.fetchall()

    print("Sent emails are", emails)
    conn.close()
    return emails


