Project Management Notification & Activity Tracking System

## Overview

This project is an enhanced Project Management application built using **FastAPI**, **SQLAlchemy ORM**, **PostgreSQL**, and **JWT Authentication**.

The system provides:

- User authentication and authorization
- Project and task management
- Notification management
- Activity tracking
- Audit trail management
- Role-based access control

The main objective is to implement an event-driven system that tracks important user actions and maintains complete history of changes.

---

# Technologies Used

- Python 3.x
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Pydantic
- JWT Authentication
- Alembic Migration
- Passlib (Password Hashing)
- Uvicorn

---

# Project Structure


project_management/

│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── oauth2.py
├── dependencies.py
├── utils.py
│
├── routers/
│ ├── auth.py
│ ├── users.py
│ ├── notifications.py
│ ├── activities.py
│ └── audit_logs.py
│
├── services/
│ ├── activity_service.py
│ ├── notification_service.py
│ └── audit_service.py
│
├── alembic/
│
├── requirements.txt
└── README.md


---

# Features

## Authentication

Implemented using JWT Authentication.

Features:

- User Registration
- User Login
- Current User Profile
- Logout Activity Tracking
- Password Hashing using bcrypt


---

# User Management

APIs:


GET /users
GET /users/me
GET /users/{id}
PUT /users/{id}
DELETE /users/{id}


Supports:

- Role-based access
- User profile update
- User activity tracking


---

# Notification System

The system automatically manages user notifications.

Notification events:

- Task Assigned
- Task Reassigned
- Task Completed
- Project Updated
- New Project Member Added


Notification APIs:


GET /notifications
GET /notifications/unread
PUT /notifications/{id}/read
PUT /notifications/read-all
DELETE /notifications/{id}


---

# Activity Log System

Tracks important user activities.

Examples:

- User Login
- User Logout
- Project Creation
- Project Update
- Task Creation
- Task Assignment
- Status Change


Activity APIs:


GET /activities
GET /activities/user/{id}
GET /activities/project/{id}
GET /activities/filter


---

# Audit Trail

Maintains complete change history.

Stores:

- Entity Type
- Entity ID
- Field Name
- Previous Value
- New Value
- Changed User
- Changed Time


Audit APIs:


GET /audit-logs
GET /audit-logs/{entity_type}/{entity_id}
GET /audit-logs/user/{user_id}


---

# Database Design

Main tables:

## Users


id
full_name
email
password
role
is_active
created_at


## Notifications


id
user_id
title
message
is_read
created_at


## Activity Logs


id
user_id
action
entity_type
entity_id
description
created_at


## Audit Logs


id
entity_type
entity_id
field_name
old_value
new_value
changed_by
changed_at


---

# Installation

Clone repository:

```bash
git clone <repository-url>

Move into project:

cd project_management

Create virtual environment:

python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Database Configuration

Create PostgreSQL database:

project_management

Update database URL in:

database.py

Example:

postgresql://username:password@localhost/project_management
Alembic Migration

Initialize migration:

alembic init alembic

Create migration:

alembic revision --autogenerate -m "initial migration"

Apply migration:

alembic upgrade head
Run Application

Start FastAPI server:

uvicorn main:app --reload

Application runs at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
Authentication Flow
Register user
POST /auth/register
Login
POST /auth/login
Copy JWT token
Click Authorize in Swagger
Enter:
Bearer <token>
API Documentation

Swagger UI:

/docs

ReDoc:

/redoc
Future Enhancements
Email Notifications
Real-time Notifications using WebSockets
Notification Preferences
CSV/PDF Export
Soft Delete Support

Author
Tamilselvi

Project Management Notification & Activity Tracking System
