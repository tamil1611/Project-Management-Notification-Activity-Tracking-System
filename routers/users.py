from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
import oauth2

from database import get_db
from dependencies import admin_manager
from services.activity_service import create_activity


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)
print("Router created:",router)

# Get all users
@router.get(
    "/",
    response_model=list[schemas.UserResponse]
)
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(admin_manager)
):

    users = (
        db.query(models.User)
        .all()
    )

    return users


# Get current logged-in user
@router.get(
    "/me",
    response_model=schemas.UserResponse
)
def get_my_profile(
    current_user=Depends(oauth2.get_current_user)
):

    return current_user


# Get user by id
@router.get(
    "/{user_id}",
    response_model=schemas.UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


# Update user
@router.put(
    "/{user_id}",
    response_model=schemas.UserResponse
)
def update_user(
    user_id: int,
    user_data: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    # Only admin/manager or own profile update
    if (
        current_user.id != user_id
        and current_user.role not in ["admin", "manager"]
    ):
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )


    old_data = {}

    for key, value in user_data.model_dump(
        exclude_unset=True
    ).items():

        old_data[key] = getattr(user, key)

        setattr(user, key, value)


    db.commit()
    db.refresh(user)


    create_activity(
        db=db,
        user_id=current_user.id,
        action="USER_UPDATED",
        entity_type="User",
        entity_id=user.id,
        description=f"{current_user.full_name} updated user {user.full_name}"
    )


    return user



# Delete user
@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_manager)
):

    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )


    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    db.delete(user)
    db.commit()


    create_activity(
        db=db,
        user_id=current_user.id,
        action="USER_DELETED",
        entity_type="User",
        entity_id=user_id,
        description=f"{current_user.full_name} deleted user {user.full_name}"
    )


    return {
        "message": "User deleted successfully"
    }