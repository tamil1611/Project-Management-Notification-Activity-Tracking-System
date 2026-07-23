Notification & Activity Tracking System

## Project Overview

This project is built using *FastAPI* and extends the Project Management API by implementing:

- User Authentication & Authorization (JWT)
- Role-Based Access Control (RBAC)
- Notification System
- Activity Tracking
- Audit Logging
- PostgreSQL Database
- SQLAlchemy ORM
- Pydantic Validation

---

## Features

### Authentication
- User Registration
- User Login
- JWT Authentication
- Get Current User
- User Logout

### User Management
- Get All Users (Admin/Manager)
- Get User by ID
- Get Current User Profile
- Update User
- Delete User

### Notification System
- Create Notifications
- Get My Notifications
- Mark Notification as Read

### Activity Tracking
- Record User Activities
- View Activity Logs
- Filter Activities by Date

### Audit Logs
- View Audit Logs
- Filter Audit Logs
- View Audit History for Specific Entity

---

## Technologies Used

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT Authentication
- Passlib (bcrypt)
- Uvicorn

---

## Project Structure


notification_and_activity_tracking_system/
│
├── routers/
│   ├── auth.py
│   ├── users.py
│   ├── notification.py
│   ├── activities.py
│   └── audit_log.py
│
├── services/
│   ├── activity_service.py
│   ├── notification_service.py
│   └── audit_service.py
│
├── models.py
├── schemas.py
├── database.py
├── oauth2.py
├── dependencies.py
├── utils.py
├── main.py
└── README.md


---

## Installation

### Clone Repository

bash
git clone <repository-url>


### Create Virtual Environment

bash
python -m venv venv


### Activate Virtual Environment

Windows

bash
venv\Scripts\activate


Linux/Mac

bash
source venv/bin/activate


### Install Dependencies

bash
pip install -r requirements.txt


### Run Application

bash
uvicorn main:app --reload


---

## API Documentation

Swagger UI


http://127.0.0.1:8000/docs


ReDoc


http://127.0.0.1:8000/redoc


---

## API Endpoints

### Authentication

- POST /auth/register
- POST /auth/login
- GET /auth/me
- POST /auth/logout

### Users

- GET /users
- GET /users/me
- GET /users/{user_id}
- PUT /users/{user_id}
- DELETE /users/{user_id}

### Notifications

- GET /notifications
- PUT /notifications/{notification_id}/read

### Activities

- GET /activities
- GET /activities/filter

### Audit Logs

- GET /audit_logs
- GET /audit_logs/{entity_type}/{entity_id}

---

## Authentication

Login using:


POST /auth/login


Copy the JWT access token.

Click *Authorize* in Swagger.

Enter:


Bearer your_access_token


Now all protected endpoints can be accessed.

---

## Database

- PostgreSQL
- SQLAlchemy ORM

---

## Author

Tamil Selvi

FastAPI Backend Developer Assignment