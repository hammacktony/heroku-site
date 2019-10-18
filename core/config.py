""" Config settings """
import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

STATIC_ROOT: str = "./web/dist/app/static"
API_V1_STR: str = "/api"

DEBUG: bool = True if os.getenv("DEBUG", "").lower() == "true" else False

SECRET_KEY: str = str(os.getenvb(b"SECRET_KEY", os.urandom(32)))

ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

BACKEND_CORS_ORIGINS: Optional[str] = os.getenv("CORS")
SENTRY_DSN: Optional[str] = os.getenv("SENTRY_DSN")

MONOGO_URI: Optional[str] = os.getenv("MONGO_URI")
MONGO_DB: str = os.getenv("MONGO_DB", "test")
MONGO_HOST: str = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT: int = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER: str = os.getenv("MONGO_USER", "")
MONGO_PWD: str = os.getenv("MONGO_PWD", "")
