from app.models import User, UserCreate, UserUpdate


# Simula una tabla en una base de datos.
# IMPORTANTE: los cambios se pierden cuando el proceso se reinicia.
_users: list[User] = [
    User(id=1, name="Ana", email="ana@example.com"),
    User(id=2, name="Carlos", email="carlos@example.com"),
    User(id=3, name="Lucia", email="lucia@example.com"),
]


def create_user(data: UserCreate) -> User:
    next_id = max((user.id for user in _users), default=0) + 1
    user = User(id=next_id, **data.model_dump())
    _users.append(user)
    return user


def get_all_users() -> list[User]:
    return _users


def get_user_by_id(user_id: int) -> User | None:
    return next((user for user in _users if user.id == user_id), None)


def update_user(user_id: int, data: UserUpdate) -> User | None:
    user = get_user_by_id(user_id)
    if user is None:
        return None

    user.name = data.name
    user.email = data.email
    return user


def delete_user(user_id: int) -> bool:
    user = get_user_by_id(user_id)
    if user is None:
        return False

    _users.remove(user)
    return True
