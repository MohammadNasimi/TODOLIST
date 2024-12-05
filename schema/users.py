from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

