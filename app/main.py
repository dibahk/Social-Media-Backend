from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth

models.Base.metadata.create_all(bind= engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host= 'localhost', database= 'fastAPI database', user= 'postgres', password= 'diba1379', cursor_factory=RealDictCursor) #readdictcursor gonna give the column names.
        cursor = conn.cursor() # for executing sql statemenets
        print('database connection was successful')
        break
    except Exception as error:
        print("connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

models.Base.metadata.create_all(bind= engine)    

my_posts = [{"title": "title of post 1", "content": "content of post 1", "ID": 1},
            {"title": "favorite food", "content": "pizza", "ID": 3}]
def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p['ID'] == id:
            return i
        
# including all the routers in post
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "welcome to my API"}
