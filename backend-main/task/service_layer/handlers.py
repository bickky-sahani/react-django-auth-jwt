import typing
from django.db import transaction

from task.service_layer import views
from task.adapters import repository
from task.domain import models, commands


def create_task(cmd: commands.AddTask, user):
    task = models.create_task_factory(
        title=cmd.title,
        description=cmd.description,
    )
    with transaction.atomic():
        repo = repository.TaskSQLRepository()
        repo.create(task=task, user=user)


def update_task(cmd: commands.UpdateTask, user, id):
    task = models.update_task_factory(
        title=cmd.title, description=cmd.description, completed=cmd.completed
    )
    with transaction.atomic():
        repo = repository.TaskSQLRepository()
        repo.update(task=task, user=user, id=id)
