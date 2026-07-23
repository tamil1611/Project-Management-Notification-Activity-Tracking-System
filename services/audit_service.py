from sqlalchemy.orm import Session
import models

def create_audit_log(
    db:Session,
    entity_type:str,
    entity_id:int,
    field_name:str,
    old_value,
    new_value,
    changed_by:int
):
    """"Create Audit Log"""
    audit= models.AuditLog(
        entity_type=entity_type,
        entity_id=entity_id,
        field_name=field_name,
        old_value=str(old_value)if old_value is not None else None,
        new_value=str(new_value)if new_value is not None else None,
        changed_by=changed_by
    )
    
    db.add(audit)
    db.commit()
    db.refresh(audit)
    return audit

def get_all_audit_logs(
    db:Session
):
    return(
        db.query(models.AuditLog)
        .order_by(models.AuditLog.changed_at.desc())
        .all()
    )

def get_entity_audit_log(
    db:Session,
    entity_type:str,
    entity_id:int
):
    return(
        db.query(models.AuditLog)
        .filter(models.AuditLog.entity_type==entity_type,
                models.AuditLog.entity_id==entity_id)
        .order_by(models.AuditLog.changed_at.desc())
        .all()
    )
    
def get_user_audit_logs(
    db:Session,
    user_id:int
):
    return(
        db.query(models.AuditLog)
        .filter(models.AuditLog.changed_by==user_id)
        .order_by(models.AuditLog.changed_at.desc())
        .all()
    )
    
def delete_audit_log(
    db:Session,
    audit_id:int
):
    audit=(
        db.query(models.AuditLog)
        .filter(models.AuditLog.id==audit_id)
        .first()
    )
    if audit:
        db.delete(audit)
        db.commit()
        return audit