from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
from resources.strings import USER_DOES_NOT_EXIST_ERROR, USER_DELETE_SUCCESSFUL
import bcrypt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def get_user(db: Session, user_id: int):
    return db.query(models.ILPUser).filter(models.ILPUser.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.ILPUser).filter(models.ILPUser.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ILPUser).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.ILPUserBase):
    db_user = models.ILPUser(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: str):
    db_user = db.query(models.ILPUser).filter(models.ILPUser.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail=USER_DOES_NOT_EXIST_ERROR)
    db.delete(db_user)
    db.commit()
    return {"message": USER_DELETE_SUCCESSFUL}


