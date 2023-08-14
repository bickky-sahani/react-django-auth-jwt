from django.contrib import auth
from account.models import CustomUser


def check_user_with_this_email_already_exist(email):
    email = CustomUser.objects.filter(email=email)
    if email:
        return True

