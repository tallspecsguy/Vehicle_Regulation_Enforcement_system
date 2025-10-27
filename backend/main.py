from fastapi import FastAPI
from routes.mail_routes import mail_router

app = FastAPI(
        title="Vehicle Regulation System API",
        description="Backend service for vehicle detection and RTO email notifications",
        version="1.0.0",
    )

app.include_router(mail_router, prefix="/api/mail", tags=["Mail"])

@app.get("/")
async def index():
    return {"status":"fastapi running successfully"}

