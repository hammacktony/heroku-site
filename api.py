""" Launch """
import os
from typing import List

from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from core.config import API_V1_STR, BACKEND_CORS_ORIGINS, DEBUG, SENTRY_DSN, STATIC_ROOT
from routes import blog, index, user

# Disable doc urls in production
docs_url, redoc_url = ("/docs", "/redoc") if DEBUG else (None, None)

__all__ = ["app"]


def routing(app: FastAPI) -> FastAPI:
    """ Declare routes """
    static_router = APIRouter()  # Handle static routes
    static_router.include_router(index.router, tags=["home"])
    api_router = APIRouter()  # Handle api routes
    api_router.include_router(blog.router, prefix="/blog", tags=["blog"])
    api_router.include_router(user.router, prefix="/user", tags=["test"])

    # Mount routers
    app.include_router(static_router)
    app.include_router(api_router, prefix=API_V1_STR)

    return app


def middleware(app: FastAPI) -> FastAPI:
    """ Enable Middleware """

    # Enable GZIP Middleware
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # Enable CORS Middleware
    if BACKEND_CORS_ORIGINS:
        origins: List[str] = list()
        origins_raw = BACKEND_CORS_ORIGINS.split(",")
        for origin in origins_raw:
            use_origin = origin.strip()
            origins.append(use_origin)
        app.add_middleware(
            CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
        )

    # Enable Sentry Middleware
    if SENTRY_DSN:
        import sentry_sdk
        from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

        sentry_sdk.init(dsn=SENTRY_DSN)
        app.add_middleware(SentryAsgiMiddleware)

    return app


# Set up app
app = FastAPI(
    title="Tony Hammack", openapi_url="/api/v1/openapi.json", docs_url=docs_url, redoc_url=redoc_url, debug=DEBUG
)
app.mount("/static", StaticFiles(directory=STATIC_ROOT), name="static")

# Routing
app = routing(app)

# Middleware
app = middleware(app)
