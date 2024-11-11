from http import HTTPStatus

from sqlalchemy.exc import SQLAlchemyError, IntegrityError


class Error(Exception):
    def __init__(self, status: int, message: str):
        self.http_status = status
        self.message = message
        super().__init__(self.message)


class SQLDefaultError(Error):
    def __init__(self, err: SQLAlchemyError):
        super().__init__(HTTPStatus.INTERNAL_SERVER_ERROR, str(err))


class SQLConstraintError(Error):
    def __init__(self, err: IntegrityError):
        super().__init__(HTTPStatus.CONFLICT, str(err.orig))


InvalidCredentialsErr = Error(HTTPStatus.UNAUTHORIZED, "INVALID CREDENTIALS")
