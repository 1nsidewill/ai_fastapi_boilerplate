import uuid
from fastapi import Request
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware
from itsdangerous import Signer, BadSignature

class SessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, secret_key: str):
        super().__init__(app)
        self.secret_key = secret_key
        self.signer = Signer(secret_key)
        self.sessions = {}  # In-memory session store

    async def dispatch(self, request: Request, call_next):
        session_id = request.cookies.get("session_id")
        session_data = {}

        if session_id:
            try:
                session_id = self.signer.unsign(session_id).decode()
                session_data = self.sessions.get(session_id, {})
            except BadSignature:
                session_id = None

        if not session_id:
            session_id = str(uuid.uuid4())
            signed_session_id = self.signer.sign(session_id).decode()
            response = Response()
            response.set_cookie("session_id", signed_session_id, httponly=True, secure=True)
            request.state.new_session = True
        else:
            signed_session_id = self.signer.sign(session_id).decode()
            request.state.new_session = False

        request.state.session_id = session_id
        request.state.session_data = session_data

        # Endpoint 진입
        response = await call_next(request)

        self.sessions[session_id] = request.state.session_data
        response.set_cookie("session_id", signed_session_id, httponly=True, secure=True)
        return response