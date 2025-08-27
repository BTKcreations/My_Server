from pydantic import BaseModel

class User(BaseModel):
    __tablename__ = "users"
    Name: str = None
    Age: int = None
    Email: str = None