class InvalidCredentialsError(Exception):
    def __init__(self):
        super().__init__("Invalid User Credentials")


class UserAuthenticationError(Exception):
    def __init__(self):
        super().__init__("User Authentication Error")


class RoleAuthenticationError(Exception):
    def __init__(self):
        super().__init__("Role Authentication Error")

        "User Authentication Error"
