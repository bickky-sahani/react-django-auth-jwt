from django.contrib import auth

from task.domain import models
from task.models import Task

from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class TaskSQLRepository:
    def __init__(self):
        pass

    def create(self, user, task: models.Task):
        Task.objects.create(
            title=task.title, description=task.description, created_by=user
        )

    def update(self, user, id, task: models.UpdateTask):
        Task.objects.filter(id=id).update(
            title=task.title, description=task.description, completed=task.completed
        )
