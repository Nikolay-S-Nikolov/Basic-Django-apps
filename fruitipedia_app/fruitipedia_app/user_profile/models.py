from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.user_profile.validators import profile_name_validator, profile_password_validator


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            profile_name_validator,
        ])

    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            profile_name_validator,
        ])

    email = models.EmailField(
        max_length=40,
        unique=True,
    )

    password = models.CharField(
        max_length=20,
        validators=[profile_password_validator],
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        null=False,
        blank=True,
        default=18,
    )
