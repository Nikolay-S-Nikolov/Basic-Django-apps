from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed_app.car.validators import car_year_validator
from world_of_speed_app.user_profile.models import Profile


# Create your models here.

class CarTypeChoices(models.TextChoices):
    RALLY = "Rally"
    OPEN_WHEEL = "Open-wheel"
    KART = "Kart"
    DRAG = "Drag"
    OTHER = "Other"


class Car(models.Model):
    MAX_TYPE_LENGTH = 10
    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1
    MIN_PRICE_VALUE = 1.0

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=CarTypeChoices.choices,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=[MinLengthValidator(MIN_MODEL_LENGTH)]
    )

    year = models.PositiveIntegerField(
        validators=[car_year_validator]
    )

    image_url = models.URLField(
        unique=True,
        error_messages={"unique": "This image URL is already in use! Provide a new one."},
        verbose_name="Image URL",
    )

    price = models.FloatField(
        validators=[MinValueValidator(MIN_PRICE_VALUE)]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )


