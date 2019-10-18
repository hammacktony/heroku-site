""" Blog Resource """
from enum import Enum
from typing import List

from fastapi import APIRouter

from core.db import db
from core.models import PostModel

router = APIRouter()
order = -1  # DESCENDING

# Denote different blogs supported
class Blog(str, Enum):
    personal: str = "personal"
    tech: str = "tech"


@router.get("/{blog}", response_model=List[PostModel])
async def index(blog: Blog):
    """ View all blogs """
    cursor = db[blog].find().sort("updated_at", order)
    retval = [doc async for doc in cursor]
    return retval


@router.get("/{blog}/{slug}", response_model=List[PostModel])
async def show(blog: Blog, slug: str):
    """ View post """
    data = await db[blog].find({"slug": slug}).to_list(length=1)
    return data
