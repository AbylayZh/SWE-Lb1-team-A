from http import HTTPStatus

from fastapi import Depends, Request, APIRouter, Response, HTTPException

from internal.handlers.endpoints import url_pending_users, url_active_users, url_inactive_users, url_admin_users
from internal.handlers.errors import InternalServerHandler
from internal.repository.models.errors import NotFoundError
from internal.service.services import Services, services
from internal.service.user.json import UserJson

router = APIRouter()


@router.get(url_pending_users)
def PendingUsersHandler(req: Request, service: Services = Depends(services)):
    try:
        unapproved_users = service.user_service.GetUnapprovedAll()
        response = {"unapproved_users": [UserJson(user) for user in unapproved_users]}

        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.get(url_active_users)
def ActiveUsersHandler(req: Request, service: Services = Depends(services)):
    try:
        active_users = service.user_service.GetActiveAll()
        response = {"active_users": [UserJson(user) for user in active_users]}

        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.get(url_inactive_users)
def InactiveUsersHandler(req: Request, service: Services = Depends(services)):
    try:
        inactive_users = service.user_service.GetInactiveAll()
        response = {"inactive_users": [UserJson(user) for user in inactive_users]}

        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.get(url_admin_users + "/{id}")
def GetUserHandler(id: int, req: Request, service: Services = Depends(services)):
    try:
        user = service.user_service.Get(id)
        response = {"user": UserJson(user)}

        return service.render(req, response)
    except NotFoundError:
        raise HTTPException(status_code=404)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.delete(url_admin_users + "/delete/{id}")
def DeleteUserHandler(id: int, req: Request, resp: Response, service: Services = Depends(services)):
    try:
        service.user_service.Delete(id)

        resp.status_code = HTTPStatus.SEE_OTHER.value
        response = {"message": "OK", "redirect_url": url_pending_users}
        return service.render(req, response)
    except NotFoundError:
        raise HTTPException(status_code=404)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.put(url_admin_users + "/approve/{id}")
def ApproveUserHandler(id: int, req: Request, resp: Response, service: Services = Depends(services)):
    try:
        service.user_service.Approve(id)

        resp.status_code = HTTPStatus.SEE_OTHER.value
        response = {"message": "OK", "redirect_url": url_pending_users}
        return service.render(req, response)
    except NotFoundError:
        raise HTTPException(status_code=404)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.put(url_admin_users + "/enable/{id}")
def EnableUserHandler(id: int, req: Request, resp: Response, service: Services = Depends(services)):
    try:
        service.user_service.Enable(id)

        resp.status_code = HTTPStatus.SEE_OTHER.value
        response = {"message": "OK", "redirect_url": url_inactive_users}
        return service.render(req, response)
    except NotFoundError:
        raise HTTPException(status_code=404)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.put(url_admin_users + "/disable/{id}")
def DisableUserHandler(id: int, req: Request, resp: Response, service: Services = Depends(services)):
    try:
        service.user_service.Disable(id)

        resp.status_code = HTTPStatus.SEE_OTHER.value
        response = {"message": "OK", "redirect_url": url_active_users}
        return service.render(req, response)
    except NotFoundError:
        raise HTTPException(status_code=404)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)
