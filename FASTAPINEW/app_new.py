from fastapi import FastAPI

from models_new import EmailRequest
from database_new import send_to_sql
from sent_db_new import get_sent_emails
from view_db_new import get_allemails
from database_new import get_pending_emails

app = FastAPI()


@app.post("/schedule")
def schedule(data: EmailRequest):

    send_to_sql(data)

    return {
        "message": "Email Scheduled Successfully"
    }

@app.get("/sent")
def callsent_emails():
    sent = get_sent_emails()
    return sent

@app.get("/allemails")
def callallemails():
    all_emails = get_allemails()
    return all_emails

@app.get("/scheduled")
def callpendingemails():
    pending_emails = get_pending_emails()
    return pending_emails

   

    
    