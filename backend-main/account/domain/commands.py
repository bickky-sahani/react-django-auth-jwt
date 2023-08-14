import typing
from dataclasses import dataclass
from pydantic import constr


class Command:
    pass


@dataclass
class AddUser(Command):
    email: typing.Optional[constr(strip_whitespace=True, max_length=255)]
    password: constr(strip_whitespace=True, min_length=8, max_length=150)


@dataclass
class LoginUser(AddUser):
    pass
