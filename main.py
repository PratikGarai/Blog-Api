from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index(): 
    return {
        "status" : "Success", 
        "message " : "Hello world!"
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