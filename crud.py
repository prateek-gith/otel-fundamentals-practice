from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate
):

    user = get_user(db, user_id)

    if not user:
        return None

    if user_data.name:
        user.name = user_data.name

    if user_data.email:
        user.email = user_data.email

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user