from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 3
    MIN_AGE_VALUE = 21
    MAX_PASSWORD_LENGTH = 20
    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 25

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[MinLengthValidator(
            limit_value=MIN_USERNAME_LENGTH,
            message="Username must be at least 3 chars long!", ),
            RegexValidator(
                regex=r"^[\w]+$",
                message="Username must contain only letters, digits, and underscores!", )
        ]
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(MIN_AGE_VALUE)
        ],
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name="First Name"
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name="Last Name"
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name="Profile Picture"
    )


