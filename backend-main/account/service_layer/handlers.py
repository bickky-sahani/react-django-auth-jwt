import typing
from django.db import transaction

from account.service_layer import views
from account.adapters import repository
from account.domain import models, commands


def register_user(cmd: commands.AddUser):
    if views.check_user_with_this_email_already_exist(email=cmd.email):
        raise Exception("User with this email already exists")

    user = models.register_user_factory(
        email=cmd.email,
        password=cmd.password,
    )
    with transaction.atomic():
        repo = repository.CustomUserSQLRepository()
        repo.register(user=user)


def login_user(cmd: commands.LoginUser):
    user = models.login_user_factory(
        email=cmd.email,
        password=cmd.password,
    )
    with transaction.atomic():
        repo = repository.CustomUserSQLRepository()
        user = repo.login(user=user)
        return user
