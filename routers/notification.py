

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
import oauth2

from database import get_db
from services import notification_service


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

print("NOTIFICATION ROUTER LOADED")
# Get all notifications of current user
@router.get(
    "/",
    response_model=list[schemas.NotificationResponse]
)
def get_notifications(
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    notifications = notification_service.get_notifications(
        db=db,
        user_id=current_user.id
    )

    return notifications



# Get unread notifications
@router.get(
    "/unread",
    response_model=list[schemas.NotificationResponse]
)
def get_unread_notifications(
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    notifications = notification_service.get_unread_notifications(
        db=db,
        user_id=current_user.id
    )

    return notifications



# Mark one notification as read
@router.put("/{notification_id}/read")
def mark_notification_as_read(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    notification = notification_service.mark_as_read(
        db=db,
        notification_id=notification_id,
        user_id=current_user.id
    )

    if notification is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notification not found"
        )

    return notification



# Mark all notifications as read
@router.put(
    "/read-all"
)
def mark_all_notifications_read(
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    notifications = notification_service.mark_all_as_read(
        db=db,
        user_id=current_user.id
    )

    return {
        "message": "All notifications marked as read",
        "count":len("notifications")
    }



# Delete notification
@router.delete(
    "/{notification_id}"
)
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    notification = notification_service.delete_notification(
        db=db,
        notification_id=notification_id,
        user_id=current_user.id
    )

    if notification is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notification not found"
        )

    return {
        "message": "Notification deleted successfully"
    }