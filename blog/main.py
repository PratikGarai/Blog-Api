from typing import final
from fastapi import FastAPI, Depends, status, Response
import uvicorn

from schemas import Blog
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()


@app.post(
    '/blog', 
    status_code=status.HTTP_201_CREATED
)
def create(request:Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)   # get stuff like id generated by the database
    return new_blog


@app.get(
    '/blog'
)
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get(
    '/blog/{id}',
     status_code=200
)
def get_single_blog(id:int, response : Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message" : f"Blog with id {id} not available"
        }
    return blog


@app.delete(
    '/blog/{id}', 
    status_code=status.HTTP_204_NO_CONTENT, 
)
def destroy(id:int, response : Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message" : f"Blog with id {id} not available"
        }
    db.query(models.Blog).filter(models.Blog.id==id).delete()
    db.commit()


@app.put(
    '/blog/{id}', 
    status_code=status.HTTP_202_ACCEPTED, 
)
def edit(id:int, request : Blog, response : Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==id)
    if(len(blogs.all())==0):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message" : f"Blog with id {id} not available"
        }
    blogs.update(
        {
            "title" : request.title, 
            "body" : request.body
        }, 
        synchronize_session=False
    )
    db.commit()
    return {
        "message" : "Blog Updated"
    }


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")