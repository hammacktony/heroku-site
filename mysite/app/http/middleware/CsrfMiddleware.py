"""CSRF Middleware."""

from masonite.middleware import CsrfMiddleware as Middleware


class CsrfMiddleware(Middleware):
    """Verify CSRF Token Middleware."""

    exempt = [
        '/api/blog/*',
    ]
    every_request = False
    token_length = 30
