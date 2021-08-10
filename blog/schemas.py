from typing import List, Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title : str
    body : str
    user_id : int


class User(BaseModel):
    name : str
    email : str
    password : str


class ShowBlog(Blog):
    id : int
    name : str
    email : str
    author : User

    class Config() :
        orm_mode = True


class UserBlog(BaseModel):
    id : int
    title : str
    body : str

    class Config() : 
        orm_mode = True


class ShowUser(BaseModel):
    name : str
    email : str
    blogs : List[UserBlog]

    class Config() :
        orm_mode = True


class MessageSchema(BaseModel):
    message : str