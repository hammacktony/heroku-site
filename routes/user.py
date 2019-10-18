""" User Resource """
from typing import List

from fastapi import APIRouter

from core.db import db
from core.models import UserModel

router = APIRouter()


@router.get("/{user}", response_model=List[UserModel])
async def show(user: str):
    data = await db["user"].find({"user_name": user}).to_list(length=1)
    return data
