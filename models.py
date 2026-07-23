from sqlalchemy import(Column,String,Integer,Text,Boolean,DateTime,ForeignKey,Table)
from sqlalchemy.orm import relationship
from database import Base

from datetime import datetime, timezone

project_members=Table("project_members",Base.metadata,
                      Column("project_id",Integer,ForeignKey("projects.id")),
                      Column("user_id",Integer,ForeignKey("users.id"))
                      )

#user model

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    full_name=Column(String(100),nullable=False)
    email=Column(String(100),unique=True,nullable=False)
    password=Column(String(255),nullable=False)
    role=Column(String(20),default="employee")
    is_active=Column(Boolean,default=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
   
    
    
    projects_created=relationship(
    "Project",
    back_populates="owner"
    )

    assigned_tasks=relationship(
    "Task",
    foreign_keys="Task.assigned_to",
    back_populates="assigned_user"
    )

    notifications=relationship(
    "Notification",
    back_populates="user",
    cascade="all,delete"
   )

    activities=relationship(
    "ActivityLog",
    back_populates="user",
    cascade="all,delete"
    )

class Project(Base):
    __tablename__="projects"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    description=Column(Text)
    status=Column(String(20),default="Active")
    created_at=Column(DateTime,default=datetime.now(timezone.utc))
    owner_id=Column(Integer,ForeignKey("users.id"))
    
    #relationship
    
    owner=relationship(
        "User",
        back_populates="projects_created"
    )
    tasks=relationship(
        "Task",
        back_populates="project",
        cascade="all,delete"
    )
    
    members=relationship(
        "User",
        secondary=project_members,
        backref="projects"
    )
    
#task model

class Task(Base):
    __tablename__="tasks"
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(150),nullable=False)
    description=Column(Text)
    status=Column(String(30),default="Pending")
    priority=Column(String(20),default="Medium")
    deadline=Column(DateTime,nullable=True)
    created_at=Column(DateTime,default=datetime.now(timezone.utc))
    project_id=Column(Integer,ForeignKey("projects.id"))
    assigned_to=Column(Integer,ForeignKey("users.id"))
    created_by=Column(Integer,ForeignKey("users.id"))
    
#relationship

    project=relationship(
    "Project",
    back_populates="tasks"
    )

    assigned_user=relationship(
        "User",
        foreign_keys="Task.assigned_to",
        back_populates="assigned_tasks"
    )

    creator=relationship(
        "User",
        foreign_keys="Task.created_by"
    )

#notification model

class Notification(Base):
    __tablename__="notifications"
    
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    title=Column(String(200),nullable=False)
    message=Column(Text,nullable=False)
    is_read=Column(Boolean,default=False)
    created_at=Column(DateTime,default=datetime.now(timezone.utc))
    
    #relationship
    
    user=relationship("User",back_populates="notifications")
    
#activity log model

class ActivityLog(Base):
    __tablename__="activity_logs"
    
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    action=Column(String(100),nullable=False)
    entity_type=Column(String(50),nullable=False)
    entity_id=Column(Integer,nullable=False)
    description=Column(Text,nullable=False)
    created_at=Column(DateTime,default=datetime.now(timezone.utc))
    
    #relationship
    
    user=relationship(
        "User",
        back_populates="activities"
    )
    
#audit log model

class AuditLog(Base):
    __tablename__="audit_logs"
    
    id=Column(Integer,primary_key=True,index=True)
    entity_type=Column(String(50),nullable=False)
    entity_id=Column(Integer,nullable=False)
    field_name=Column(String(100),nullable=False)
    old_value=Column(Text)
    new_value=Column(Text)
    changed_by=Column(Integer,ForeignKey("users.id"))
    changed_at=Column(DateTime,default=datetime.now(timezone.utc))
    
    #relationship
    
    changed_user=relationship("User")
    

