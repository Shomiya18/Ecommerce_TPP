from sqlalchemy.orm import Session

from app.db.models import User

def get_all_users(db: Session) -> list[User]:
    return db.query(User).order_by(User.id).all()

def get_user_by_id(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def update_admin_status(db: Session, user_id: int, is_admin: bool)-> User:
    user = get_user_by_id(db,user_id)
    user.is_admin = is_admin

    db.commit()
    db.refresh(user)
    return user

def delete_user(db:Session, user_id: int) -> None:
    user = get_user_by_id(db, user_id)

    db.delete(user)
    db.commit()