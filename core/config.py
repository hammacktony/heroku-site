""" Config settings """
import os
from enum import Enum
from typing import Optional

from dotenv import load_dotenv

# User Defined
STATIC_ROOT: str = "./web/dist/app"
API_V1_STR: str = "/api"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

# Environment Defined
load_dotenv()

DEBUG: bool = True if os.getenv("DEBUG", "").lower() == "true" else False

# Define CORS
BACKEND_CORS_ORIGINS: Optional[str] = os.getenv("CORS")

# Sentry Config
SENTRY_DSN: Optional[str] = os.getenv("SENTRY_DSN")

# Show/Hide api documentation
class DOCS(Enum):
    SWAGGER: Optional[str] = "/api/docs" if DEBUG else None
    REDOC: Optional[str] = "/api/redoc" if DEBUG else None


# Mongo Config
class MONGO(Enum):
    URI: Optional[str] = os.getenv("MONGO_URI")
    DB: str = os.getenv("MONGO_DB", "test")
    HOST: str = os.getenv("MONGO_HOST", "localhost")
    PORT: int = int(os.getenv("MONGO_PORT", 27017))
    USER: str = os.getenv("MONGO_USER", "")
    PWD: str = os.getenv("MONGO_PWD", "")
