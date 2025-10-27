from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from config import settings

mail_conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=True
)

# Async mail sending function
async def send_violation_email(email: EmailStr, subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=body,
        subtype="html"
    )
    fm = FastMail(mail_conf)
    await fm.send_message(message)
    return {"message": f"Email sent to {email}"}
