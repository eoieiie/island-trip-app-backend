from pydantic import BaseModel, Field

class UserModel(BaseModel):
    username: str
    email: str
    full_name: str

    class Config:
        schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john.doe@example.com",
                "full_name": "John Doe"
            }
        }