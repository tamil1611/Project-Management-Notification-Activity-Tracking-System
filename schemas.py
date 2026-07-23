from pydantic import BaseModel,ConfigDict
from typing import Optional
from datetime import datetime

#user schemas

class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    role:str = "employee"
    
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None
    
class UserResponse(BaseModel):
    id:int
    full_name:str
    email:str
    role:str
    is_active:bool
    created_at:datetime
    
    model_config=ConfigDict(from_attributes=True)
    
    
#project schemas

class ProjectCreate(BaseModel):
    name:str
    description:Optional[str]=None
class ProjectUpdate(BaseModel):
    name:Optional[str]=None
    description: Optional[str]=None
    status:Optional[str]=None
    
class ProjectResponse(BaseModel):
    id:int
    name:str
    description:Optional[str]
    status:str
    owner_id:int
    created_at:datetime
    
    model_config=ConfigDict(from_attributes=True)
    
#task schemas

class TaskCreate(BaseModel):
    title:str
    description:Optional[str]=None
    priority:str="Medium"
    deadline:Optional[datetime]=None
    project_id:int
    assigned_to:int
    
class TaskUpdate(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    priority:Optional[str]=None
    status:Optional[str]=None
    deadline:Optional[str]=None
    assigned_to:Optional[str]=None
    
class TaskResponse(BaseModel):
    id:int
    title:str
    description:Optional[str]
    status:str
    priority:str
    deadline:Optional[datetime]
    project_id:int
    assigned_to:int
    created_by:int
    created_at:datetime
    
    model_config=ConfigDict(from_attributes=True)
    
#notification schemas

class NotificationCreate(BaseModel):
    user_id:int
    title:str
    message:str
    
class NotificationResponse(BaseModel):
    id:int
    user_id:int
    title:str
    message:str
    is_read:bool
    created_at:datetime
    
    model_config=ConfigDict(from_attributes=True)
    
#activity log schemas

class ActivityLogCreate(BaseModel):
    action:str
    entity_type:str
    entity_id:int
    description:str
    
class ActivityLogResponse(BaseModel):
    id:int
    user_id:int
    action:str
    entity_type:str
    entity_id:int
    description:str
    created_at:datetime
    
    model_config=ConfigDict(from_attributes=True)
    
#audit log schemas

class AuditLogCreate(BaseModel):
    entity_type:str
    entity_id:int
    field_name:str
    old_value:Optional[str]=None
    new_Value:Optional[str]=None
    
class AuditLogResponse(BaseModel):
    id:int
    entity_type:str
    entity_id:int
    field_name:str
    old_value:Optional[str]
    new_value:Optional[str]
    changed_by:int
    changed_at:datetime
    
    model_config=ConfigDict(from_attributes=True)
    
#authendication schemas

class UserLogin(BaseModel):
    email:str
    password:str
    
class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    id:Optional[int]=None
    
    
    
    