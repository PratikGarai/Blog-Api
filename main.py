from typing import Optional
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index(): 
    return {
        "status" : "Success", 
        "message " : "Hello world!"
    }

@app.get('/blog')
def index(limit=5, published="Yesterday", sort : Optional[str] = None): 
    return {
        "data" : "All blogs till "+str(limit) + " " +published
    }

@app.get('/blog/unpublished')
def getUnpublished():
    return {
        "data" : "All unpublished"
    }

@app.get('/blog/{id}')
def singleBlog(id : int):
    return {
        "id" : id
    }

@app.get('/blog/{id1}/comments/{id2}')
def singleBlogComment(id1 : int, id2):
    return {
        "id1" : id1,
        "id2" : id2
    }


class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]


@app.post('/blog')
def create_blog(blog : Blog) :
    return {
        "data" : "Blog is created",
        "title" : blog.title,
        "body" : blog.title,
        "pub" : blog.published_at
    }

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")