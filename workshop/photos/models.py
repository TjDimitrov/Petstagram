from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator
from workshop.photos.validators import validate_file_size
from workshop.pets.models import Pet


UserModel = get_user_model()


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=(validate_file_size,),
        null=False,
        blank=True
    )

    description = models.TextField(
        validators=(MinLengthValidator(10),),
        max_length=300,
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True
    )

    date_of_publication = models.DateField(
        auto_now=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

