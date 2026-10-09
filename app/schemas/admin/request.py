from pydantic import BaseModel,ConfigDict


class AdminRoleUpdate(BaseModel):
    is_admin: bool
