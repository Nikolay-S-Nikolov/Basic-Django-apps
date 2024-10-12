from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.fruit.validators import fruit_name_validator
from fruitipedia_app.user_profile.models import Profile


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        unique=True,
        max_length=30,
        validators=[MinLengthValidator(2), fruit_name_validator],
        error_messages={"unique": "This fruit name is already in use! Try a new one."}
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
    )
