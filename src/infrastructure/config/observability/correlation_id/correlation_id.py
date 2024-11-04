import uuid
from collections.abc import Callable
from contextvars import ContextVar
from typing import Awaitable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

correlation_id_ctx_var = ContextVar("correlation_id", default=None)


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
        correlation_id_ctx_var.set(correlation_id)  # type: ignore

        response = await call_next(request)

        response.headers["X-Correlation-ID"] = correlation_id

        return response
