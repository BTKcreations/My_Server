from fastapi import APIRouter
from models import User
router = APIRouter()

@router.get("/add")
async def add(a: int, b: int):
    return {"result": a + b}

@router.get("/mul")
async def mul(a: int, b: int):
    return {"result": a * b}
@router.get("/users")
async def usersGet(users: User):
    return users.json
