from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel, EmailStr
from services.mail_service import send_violation_email

mail_router = APIRouter()

class MailRequest(BaseModel):
    email: EmailStr
    subject: str
    body: str

@mail_router.post("/send")
async def send_mail(request: MailRequest, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(send_violation_email, request.email, request.subject, request.body)
    return {"status": "Mail scheduled for sending"}
