from fastapi import Depends, Request, APIRouter

from internal.handlers.handler import Handlers, handlers

router = APIRouter()


@router.get("/")
async def Home(req: Request, handler: Handlers = Depends(handlers)):
    session = await handler.sessions.GetCurrentSession(req)
    if not session:
        return {"auth": "no"}

    return {"auth": "yes", "user_id": session["user_id"], "role": session["role"]}
