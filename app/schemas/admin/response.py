from pydantic import BaseModel,ConfigDict


class AdminUserResponse(BaseModel):
    id: int
    user_name: str
    email: str
    is_admin: bool

    model_config = ConfigDict(from_attributes=True)