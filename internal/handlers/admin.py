from fastapi import Depends, Request, APIRouter

from internal.handlers.errors import InternalServerHandler
from internal.service.services import Services, services
from internal.service.user.json import UserJson

router = APIRouter()


@router.get("/user/admin/dashboard/pending-farmers")
async def Home(req: Request, service: Services = Depends(services)):
    try:
        unapproved_users = service.user_service.GetUnapprovedAll()

        return {"auth_user": UserJson(getattr(req.state, 'user', None)),
                "unapproved_users": [UserJson(user) for user in unapproved_users]}
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)
