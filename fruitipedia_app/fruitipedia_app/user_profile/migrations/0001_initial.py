# Generated by Django 5.1.2 on 2024-10-11 10:26

import django.core.validators
import fruitipedia_app.user_profile.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), fruitipedia_app.user_profile.validators.profile_name_validator])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), fruitipedia_app.user_profile.validators.profile_name_validator])),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=20, validators=[fruitipedia_app.user_profile.validators.profile_password_validator])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, default=18)),
            ],
        ),
    ]
