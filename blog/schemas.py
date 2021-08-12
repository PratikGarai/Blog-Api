from typing import List, Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title : str
    body : str
    user_id : int


class User(BaseModel):
    name : str
    username : str
    email : str
    password : str


class BlogAuthor(BaseModel) :
    id : int
    username : str
    name : str
    email : str

    class Config() :
        orm_mode = True


class ShowBlog(Blog):
    id : int
    title : str
    body : str
    author : BlogAuthor

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
    username : str
    email : str
    blogs : List[UserBlog]

    class Config() :
        orm_mode = True


class MessageSchema(BaseModel):
    message : str


class Login(BaseModel) :
    username : str
    password : str