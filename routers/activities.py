from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
import models
import schemas
import oauth2

from database import get_db
from services import activity_service


router = APIRouter(
    prefix="/activities",
    tags=["Activities"]
)


# Get all activities
@router.get(
    "/",
    response_model=list[schemas.ActivityLogResponse]
)
def get_all_activities(
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    return activity_service.get_all_activities(
        db=db
    )



# Get activities by user id
@router.get(
    "/user/{user_id}",
    response_model=list[schemas.ActivityLogResponse]
)
def get_user_activities(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
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



# Get project activities
@router.get(
    "/project/{project_id}",
    response_model=list[schemas.ActivityLogResponse]
)
def get_project_activities(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    return activity_service.get_project_activities(
        db=db,
        project_id=project_id
    )



# Filter activities
@router.get(
    "/filter",
    response_model=list[schemas.ActivityLogResponse]
)
def filter_activities(
    action: Optional[str] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    if action:
        return activity_service.filter_by_action(
            db=db,
            action=action
        )

    if start_date and end_date:
        return activity_service.filter_by_date(
            db=db,
            start_date=start_date,
            end_date=end_date
        )

    return activity_service.get_all_activities(
        db=db
    )