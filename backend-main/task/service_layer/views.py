from django.contrib import auth
from account.models import CustomUser


def check_user_with_this_email_already_exist(email):
    email = CustomUser.objects.filter(email=email)
    if email:
        return True


# def username_password_didnot_matched(username, password):
#     user = auth.authenticate(username=username, password=password)
#     print("inside username password check", user)
#     status = ""
#     if not user:
#         status = "invalid"
#         return status
#     if not user.is_active:
#         status = "disabled"
#         return status

#     return status
