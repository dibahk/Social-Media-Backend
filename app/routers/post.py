from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from ..database import engine, get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix= '/posts',
                   tags= ['posts'])


@router.get("/", response_model= List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # # raw SQL
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all() #grabbing every entery in post table
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # # raw SQL  
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", 
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

        

@router.get("/{id}", response_model=schemas.Post) #getting a specific post the id is a path parameter
def get_post(id: int, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first() # filter is like id
    print(post)
    if not post: #if we don't find a post
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)# filter is like id
    

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id : {id} was not found")

    post.delete(synchronize_session= False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) # for deleting no message should be sent back

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.Post, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
    #                (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id : {id} was not found")
    post_query.update(post.dict(), synchronize_session= False)
    db.commit()
    return post_query.first()