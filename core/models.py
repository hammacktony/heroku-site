""" Pydantic Models """
from typing import Optional

from pydantic import BaseModel

__all__ = ["UserModel", "PostModel"]


# User Field Declarations
class UserModel(BaseModel):
    name: str
    email: str
    bio: str
    website: str
    image: str
    twitter: Optional[str] = None
    facebook: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    gitlab: Optional[str] = None
    devto: Optional[str] = None


# Post Field Declarations
class PostModel(BaseModel):
    slug: str
    title: str
    created_at: str
    updated_at: str
    image: str
    body: str
    category: Optional[str] = None
    shortened_url: Optional[str] = None
