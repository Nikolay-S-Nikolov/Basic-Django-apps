from django.core.exceptions import ValidationError


def profile_name_validator(value: str):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def profile_password_validator(value: str):
    if len(value) < 8 or len(value) > 20:
        raise ValidationError("*Password length requirements: 8 to 20 characters")
