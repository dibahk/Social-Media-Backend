from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass #extending everything

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes= True

class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        from_attributes= True

class Token(BaseModel):
    token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]= None

class Vote(BaseModel):
    post_id: int
    dir: int = Field(..., le=1)  # Type should be int, with a validator `le=1`