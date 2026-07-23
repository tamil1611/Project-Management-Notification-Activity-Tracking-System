from fastapi import FastAPI

from database import engine, Base

from routers import auth
from routers import users
from routers import notification
from routers import activities
from routers import audit_log


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Project Management Notification System",
    description="Project Management API with Notifications, Activity Logs and Audit Trail",
    version="1.0.0"
)


# Include routers

app.include_router(
    auth.router
)

app.include_router(
    users.router
)

app.include_router(
    notification.router
)

app.include_router(
    activities.router
)

app.include_router(
    audit_log.router
)


@app.get("/")
def root():
    return {
        "message": "Project Management API is running"
    }