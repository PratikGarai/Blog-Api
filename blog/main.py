from fastapi import FastAPI
import uvicorn

from schemas import Blog

app = FastAPI()

@app.post('/blog')
def create(request:Blog):
    return "creating"


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")