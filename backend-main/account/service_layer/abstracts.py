import typing
import re
from pydantic import BaseModel, validator, constr, root_validator

# from claim_payment_act.domain.exceptions import ClaimPaymentActCannotBeEmpty


class DataModel(BaseModel):
    """base model for form data"""

    class Config:
        allow_mutation = False
        # arbitrary_types_allowed = True
        extra = "ignore"
        check_fields = False


class AddUser(DataModel):
    email: typing.Optional[constr(strip_whitespace=True, max_length=255)]
    password: constr(strip_whitespace=True, min_length=8, max_length=150)

    @root_validator(pre=True, allow_reuse=True)
    def email_must_be_valid(cls, values):
        email = values.get("email")
        if email.strip() == "" or not email or email == "":
            raise Exception("Email cannot be empty, whitespace or null")
        if len(email) >= 255:
            raise Exception("Username cannot be greater than 150 characters")
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise Exception("Invalid email format")
        return values

    @root_validator(pre=True, allow_reuse=True)
    def password_must_be_strong(cls, values):
        password = values.get("password")

        if not password or len(password) < 8:
            raise Exception("Password must be at least 8 characters long")
        if not any(char.isupper() for char in password):
            raise Exception("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise Exception("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in password):
            raise Exception("Password must contain at least one digit")

        return values


class LoginUser(DataModel):
    email: typing.Optional[constr(strip_whitespace=True, max_length=255)]
    password: constr(strip_whitespace=True, min_length=8, max_length=150)
