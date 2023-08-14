from django.contrib import auth

from account.domain import models
from account.models import CustomUser

from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class CustomUserSQLRepository:
    def __init__(self):
        pass

    def list_all_users():
        pass

    def register(self, user: models.User):
        CustomUser.objects.create_user(
            email=user.email,
            password=user.password,
        )

    def login(self, user: models.LoginUser):
        user = auth.authenticate(email=user.email, password=user.password)
        if not user:
            raise Exception("Invalid credentials, try again")
        if not user.is_active:
            raise Exception("Account disabled, contact admin")

        return user

    def get():
        pass

    def update():
        pass

    def delete():
        pass
