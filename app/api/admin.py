
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.api.deps import get_db, get_current_admin
from app.db.models import User
from app.schemas.admin.response import AdminUserResponse
from app.schemas.admin.request import AdminRoleUpdate
from app.services.admin_services import get_all_users,update_admin_status

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/users", response_model=list[AdminUserResponse])
def list_users(db: Session = Depends(get_db),admin: User = Depends(get_current_admin),):
    return get_all_users(db)


@router.patch("/users/{user_id}/role", response_model=AdminUserResponse)
def update_user_role(user_id: int, role_data: AdminRoleUpdate, db: Session = Depends(get_db), admin: User = Depends(get_current_admin),):
    
    if user_id == admin.id:
        raise HTTPException(
            status_code=400,
            detail="You cannot change your own admin role",
        )

    return update_user_admin_status(db, user_id, role_data.is_admin)