from typing import Optional
from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

my_posts = [{"title": "title of post 1", "content": "content of post 1", "ID": 1},
            {"title": "favorite food", "content": "pizza", "ID": 3}]

@app.get("/")
async def root():
    return {"message": "welcome to my API222"}
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["ID"] = randrange(0, 10000000) #every id should be unique
    my_posts.append(post_dict)
    return {"data": post_dict}
    # title str, content str, category 

def find_post(id):
    for p  in my_posts:
        if p["ID"] == id:
            return p
        
@app.get("/posts/latest")
def get_latest():
    post = my_posts[len(my_posts) - 1]
    return {"detail": post}

@app.get("/posts/{id}") #getting a specific post the id is a path parameter
def get_post(id: int, response: Response):
    post = find_post(int(id))
    if not post: #if we don't find a post
        response.status_code = 404
    return {"post_detail": post}


