from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.templatetags.static import static


def only_letters(value):
    for symbol in value:
        if not symbol.isalpha():
            raise ValidationError('Use only alphabetical letters!')


class PetstagramUser(AbstractUser):
    CHOICE_ONE = 'Male'
    CHOICE_TWO = 'Female'
    CHOICE_THREE = 'Do not show'

    CHOICES = (
        (CHOICE_ONE, 'Male'),
        (CHOICE_TWO, 'Female'),
        (CHOICE_THREE, 'Do not show'),
    )

    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField(
        unique=True,

    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            only_letters,
            MinLengthValidator(FIRST_NAME_MIN_LEN),
        ),
        blank=True
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
        ),
        blank=True
    )
    profile_picture = models.URLField(
        default=static('images/person.png')
    )

    gender = models.CharField(
        max_length=50,
        choices=CHOICES,
        default=CHOICE_ONE,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
