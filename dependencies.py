from fastapi import Depends, HTTPException, status
from oauth2 import get_current_user

class RoleChecker:
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user=Depends(get_current_user)):
        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not authorized to perform this action."
            )

        return current_user


# Role dependencies
admin_only = RoleChecker(["admin"])
manager_only = RoleChecker(["manager"])
employee_only = RoleChecker(["employee"])
admin_manager = RoleChecker(["admin", "manager"])
all_roles = RoleChecker(["admin", "manager", "employee"])