from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session

import schemas
import database
import models
import hashing

router = APIRouter(
    tags=["Auth"],
    prefix="/auth"
)
hash = hashing.Hash()

def get_db():
    db = database.SessionLocal()
    try :
        yield db
    finally :
        db.close()


@router.post(
    '/login',
    response_model=schemas.ShowUser
)
def login(
    request : schemas.Login, 
    db: Session = Depends(get_db),
) :
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        )
    if not hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        )
    return user