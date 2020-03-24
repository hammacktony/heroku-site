""" Launch """
import os
from typing import List

from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.staticfiles import StaticFiles

from core.config import API_V1_STR, BACKEND_CORS_ORIGINS, DEBUG, DOCS, SENTRY_DSN, STATIC_ROOT
from routes import blog, user

__all__ = ["app"]


def routing(app: FastAPI) -> FastAPI:
    """ Declare routes """
    router = APIRouter()
    router.include_router(blog.router, prefix="/blog", tags=["blog"])
    router.include_router(user.router, prefix="/user", tags=["user"])
    app.include_router(router, prefix=API_V1_STR)
    return app


def middleware(app: FastAPI) -> FastAPI:
    """ Enable Middleware """

    # Enable GZIP Middleware
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # Enable CORS Middleware
    if BACKEND_CORS_ORIGINS != [""]:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=BACKEND_CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Enable Sentry Middleware
    if SENTRY_DSN:
        import sentry_sdk
        from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

        sentry_sdk.init(dsn=SENTRY_DSN)
        app.add_middleware(SentryAsgiMiddleware)

    return app


def init() -> FastAPI:
    """ Create FastAPI backend  """
    app = FastAPI(
        title="Tony Hammack",
        openapi_url="/api/v1/openapi.json",
        docs_url=DOCS.SWAGGER.value,
        redoc_url=DOCS.REDOC.value,
        debug=DEBUG,
    )
    # Routing
    app = routing(app)

    # Middleware
    app = middleware(app)

    # Mount static files
    app.mount("/", StaticFiles(directory=STATIC_ROOT, html=True), name="static")
    return app


# Initiate app
app = init()
