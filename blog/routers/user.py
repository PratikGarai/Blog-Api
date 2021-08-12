from typing import List, Union
from fastapi import APIRouter, status, Depends, Response
from sqlalchemy.orm import Session

import models
import schemas
import database
import hashing

router = APIRouter(
    tags = ["User"],
    prefix="/user"
)

hash = hashing.Hash()

def get_db():
    db = database.SessionLocal()
    try :
        yield db
    finally :
        db.close()


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowUser
)
def create_user(
    request : schemas.User,
    db: Session = Depends(get_db)
):
    hashed_password = hash.bcrypt(request.password)
    request.password = hashed_password
    new_user = models.User(**request.__dict__)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get(
    '/{id}',
    response_model=Union[
        schemas.ShowUser,
        schemas.MessageSchema
    ]
)
def get_user(
    id : int,
    response : Response,
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id==id)
    if not user.first() :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message" : f"User {id} not found"
        }
    return user.first()
