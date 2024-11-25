import asyncio
import uuid
from datetime import datetime
from typing import Dict, Any

from fastapi import Request


class SessionStore:
    Store: Dict[str, Dict[str, Any]]
    ActiveSessions: Dict[int, str]

    def __init__(self):
        self.Store = {}
        self.ActiveSessions = {}
        self.Mutex = asyncio.Lock()

    async def CreateSession(self, user_id: int = None) -> str:
        session_id = str(uuid.uuid4())

        async with self.Mutex:
            if user_id:
                self.Store[session_id] = {"user_id": user_id, "last_request": datetime.utcnow()}
                self.ActiveSessions[user_id] = session_id
                return session_id

            self.Store[session_id] = {}
            return session_id

    async def GetCurrentSession(self, req: Request):
        session_id = req.cookies.get("session_id")
        if not session_id:
            return None

        async with self.Mutex:
            return self.Store.get(session_id)

    async def DeleteCurrentSession(self, req: Request):
        session_id = req.cookies.get("session_id")
        if not session_id:
            return

        async with self.Mutex:
            if session_id in self.Store:
                user_id = self.Store[session_id].get("user_id")
                if user_id:
                    self.ActiveSessions.pop(user_id, None)

            self.Store.pop(session_id, None)

    async def UpdateSessionData(self, req: Request, key: str, value: Any):
        session_id = req.cookies.get("session_id")
        if not session_id:
            session_id = await self.CreateSession()

        async with self.Mutex:
            self.Store[session_id][key] = value

    async def PopSessionFlash(self, req: Request):
        session_id = req.cookies.get("session_id")
        if not session_id:
            return None

        async with self.Mutex:
            if session_id not in self.Store:
                return None

            flash = self.Store[session_id].get("flash")
            if not flash:
                return None

            self.Store[session_id].pop("flash")
            return flash

    async def UpdateSessionRequest(self, req: Request):
        async with self.Mutex:
            await self.UpdateSessionData(req, "last_request", datetime.utcnow())
