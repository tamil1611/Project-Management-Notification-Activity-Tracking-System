
from sqlalchemy.orm import Session
import models

def create_activity(
    db:Session,
    user_id,
    action:str,
    entity_type:str,
    entity_id,
    description:str
):
    """ create an activity log entry."""
    
    activity=models.ActivityLog(user_id=user_id,
                                action=action,
                                entity_type=entity_type,
                                entity_id=entity_id,
                                description=description
                                )
    db.add(activity)
    db.commit()
    db.refresh(activity)
    
    return activity

def get_user_activities(
    db: Session,
    user_id: int
):
    return (
        db.query(models.ActivityLog)
        .filter(
            models.ActivityLog.user_id == user_id
        )
        .order_by(
            models.ActivityLog.created_at.desc()
        )
        .all()
    )

def get_project_activities(db:Session,project_id:int):
    return(db.query(models.ActivityLog)
           .filter(
               models.ActivityLog.entity_type=="Project",
               models.ActivityLog.entity_id==project_id
           )
           .order_by(models.ActivityLog.created_at.desc())
           .all())

def get_all_activies(db:Session):
    return(
        db.query(models.ActivityLog)
        .order_by(models.ActivityLog.created_at.desc())
        .all()
    )

def filter_by_action(db:Session,
                     action:str
                     ):
    return(
        db.query(models.ActivityLog)
        .filter(
            models.ActivityLog.action == action)
        .order_by(models.ActivityLog.created_at.desc())
        .all()
    )
    
def filter_by_date(
    db:Session,
    start_date,
    end_date
):
    return(
        db.query(models.ActivityLog)
        .filter(
            models.ActivityLog.created_at >=start_date,
            models.ActivityLog.created_at<=end_date)
        .order_by(models.ActivityLog.created_at.desc())
        .all()
    )