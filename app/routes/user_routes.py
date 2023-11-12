from fastapi import APIRouter, Request
from app.models.user_model import UserCreate, UserRead
from app.controllers.user_controller import user_controller

router = APIRouter()

@router.post('/register')
async def register_user(request: Request, user: UserCreate):
    result = await user_controller.register_user(user)
    return result

@router.post('/login')
async def login_user(request: Request, user: UserRead):
    result = await user_controller.login_user(user)
    return result