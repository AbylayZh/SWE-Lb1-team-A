from fastapi import Depends, Request, APIRouter

from internal.service.services import Services, services

router = APIRouter()


@router.get("/")
async def Home(req: Request, service: Services = Depends(services)):
    user = getattr(req.state, 'user', None)
    if not user:
        return {"auth": "no"}

    return {"auth": "yes", "user_id": user.id, "role": user.role}
