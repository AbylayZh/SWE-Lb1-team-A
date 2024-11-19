from internal.repository.models.users import User


def UserJson(user: User):
    if not user:
        return None

    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone": user.phone_number,
        "created": user.created,
        "approved": user.approved,
        "active": user.active,
    }
