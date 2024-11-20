from http import HTTPStatus

from fastapi import Depends, Request, APIRouter, Response

from internal.handlers.errors import InternalServerHandler
from internal.service.services import Services, services
from internal.service.user.json import UserJson

router = APIRouter()


@router.get("/user/admin/users/pending")
def PendingUsersHandler(req: Request, service: Services = Depends(services)):
    try:
        unapproved_users = service.user_service.GetUnapprovedAll()
        response = {"unapproved_users": [UserJson(user) for user in unapproved_users]}

        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.get("/user/admin/users/active")
def ActiveUsersHandler(req: Request, service: Services = Depends(services)):
    try:
        active_users = service.user_service.GetActiveAll()
        response = {"active_users": [UserJson(user) for user in active_users]}

        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.get("/user/admin/users/inactive")
def InactiveUsersHandler(req: Request, service: Services = Depends(services)):
    try:
        inactive_users = service.user_service.GetInactiveAll()
        response = {"inactive_users": [UserJson(user) for user in inactive_users]}

        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.put("/user/admin/users/approve/{id}")
def ApproveUserHandler(id: int, req: Request, resp: Response, service: Services = Depends(services)):
    try:
        service.user_service.Approve(id)

        resp.status_code = HTTPStatus.SEE_OTHER.value
        response = {"message": "OK", "redirect_url": "/user/admin/users/pending"}
        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.delete("/user/admin/users/reject/{id}")
def DeleteUserHandler(id: int, req: Request, resp: Response, service: Services = Depends(services)):
    try:
        service.user_service.Delete(id)

        resp.status_code = HTTPStatus.SEE_OTHER.value
        response = {"message": "OK", "redirect_url": "/user/admin/users/pending"}
        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.put("/user/admin/users/enable/{id}")
def EnableUserHandler(id: int, req: Request, resp: Response, service: Services = Depends(services)):
    try:
        service.user_service.Enable(id)

        resp.status_code = HTTPStatus.SEE_OTHER.value
        response = {"message": "OK", "redirect_url": "/user/admin/users/inactive"}
        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.put("/user/admin/users/disable/{id}")
def DisableUserHandler(id: int, req: Request, resp: Response, service: Services = Depends(services)):
    try:
        service.user_service.Disable(id)

        resp.status_code = HTTPStatus.SEE_OTHER.value
        response = {"message": "OK", "redirect_url": "/user/admin/users/active"}
        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)
