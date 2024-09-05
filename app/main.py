from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

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
    
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

my_posts = [{"title": "title of post 1", "content": "content of post 1", "ID": 1},
            {"title": "favorite food", "content": "pizza", "ID": 3}]
def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p['ID'] == id:
            return i
        
@app.get("/")
async def root():
    return {"message": "welcome to my API222"}
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    # 
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", 
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}
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
    cursor.execute("""SELECT * FROM posts WHERE ID = %s """, (str(id)))
    post = cursor.fetchone()
    if not post: #if we don't find a post
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id : {id} was not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT) # for deleting no message should be sent back

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_post_index(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id : {id} was not found")
    post_dict = post.dict()
    post_dict['ID'] = id
    my_posts[index] = post_dict
    print(post)
    return {'data': post_dict}
