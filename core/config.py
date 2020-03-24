""" Config settings """
import os
from enum import Enum
from typing import List, Optional

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

# User Defined
STATIC_ROOT: str = "./web/dist/app"
API_V1_STR: str = "/api"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

# Environment Defined
config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

# Define CORS
BACKEND_CORS_ORIGINS: List[str] = list(config("CORS", cast=CommaSeparatedStrings, default=""))

# Sentry Config
SENTRY_DSN: Optional[str] = config("SENTRY_DSN", cast=str, default="")

# Show/Hide api documentation
class DOCS(Enum):
    SWAGGER: Optional[str] = "/api/docs" if DEBUG else None
    REDOC: Optional[str] = "/api/redoc" if DEBUG else None


# Mongo Config
class MONGO(Enum):
    URI: Optional[str] = config("MONGO_URI", cast=str, default="")
    DB: str = config("MONGO_DB", cast=str, default="test")
    HOST: str = config("MONGO_HOST", cast=str, default="localhost")
    PORT: int = config("MONGO_PORT", cast=int, default=27017)
    USER: str = config("MONGO_USER", cast=str, default="")
    PWD: str = config("MONGO_PWD", cast=str, default="")
