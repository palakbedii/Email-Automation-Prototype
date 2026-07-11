from datetime import date, time
from pydantic import BaseModel

class EmailRequest(BaseModel):
    recipient: str
    subject: str
    message: str
    date: date
    time: time