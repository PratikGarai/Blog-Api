from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]

@app.post('/blog')
def create(request:Blog):
    return "creating"


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")