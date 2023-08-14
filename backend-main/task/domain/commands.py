import typing
from dataclasses import dataclass
from pydantic import constr, Field


class Command:
    pass


@dataclass
class AddTask(Command):
    title: constr(strip_whitespace=True, max_length=100)
    description: constr(strip_whitespace=True)


@dataclass
class UpdateTask(AddTask):
    completed: bool
