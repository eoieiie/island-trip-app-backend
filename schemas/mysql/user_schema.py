from pydantic import BaseModel

class UserBase(BaseModel):
    nickname: str
    profile_photo: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True
