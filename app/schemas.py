from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Annotated
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase):  # Inherits fields from PostBase
    pass


class UpdatePost(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:

        from_attributes = True


class PostResponse(PostBase):
    id: int
    owner_id: int
    created_at: datetime
    owner: UserOut

    class Config:

        from_attributes = True


class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:

        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]  # dir can only be 0 or 1

    class Config:
        # This allows Pydantic to read data even if it is not a dict, but an ORM model
        from_attributes = True
