import typing
from pydantic import BaseModel, constr


class Task(BaseModel):
    title: constr(strip_whitespace=True, max_length=100)
    description: constr(strip_whitespace=True)


def create_task_factory(title, description):
    return Task(
        title=title,
        description=description,
    )


class UpdateTask(Task):
    completed: bool


def update_task_factory(title, description, completed):
    return UpdateTask(
        title=title,
        description=description,
        completed=completed,
    )
