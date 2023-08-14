import typing
from pydantic import BaseModel, constr


class User(BaseModel):
    email: typing.Optional[constr(strip_whitespace=True, max_length=255)]
    password: constr(strip_whitespace=True, min_length=8, max_length=150)


def register_user_factory(email, password):
    return User(
        email=email,
        password=password,
    )


class LoginUser(User):
    pass


def login_user_factory(email, password):
    return LoginUser(
        email=email,
        password=password,
    )
