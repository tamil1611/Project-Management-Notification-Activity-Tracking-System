from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
import oauth2

from database import get_db
from services import audit_service


router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)


# Get all audit logs
@router.get(
    "/",
    response_model=list[schemas.AuditLogResponse]
)
def get_all_audit_logs(
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    return audit_service.get_all_audit_logs(
        db=db
    )



# Get audit logs by entity
@router.get(
    "/{entity_type}/{entity_id}",
    response_model=list[schemas.AuditLogResponse]
)
def get_entity_audit_logs(
    entity_type: str,
    entity_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    logs = audit_service.get_entity_audit_log(
        db=db,
        entity_type=entity_type,
        entity_id=entity_id
    )

    return logs



# Get audit logs changed by user
@router.get(
    "/user/{user_id}",
    response_model=list[schemas.AuditLogResponse]
)
def get_user_audit_logs(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):

    logs = audit_service.get_user_audit_logs(
        db=db,
        user_id=user_id
    )

    return logs