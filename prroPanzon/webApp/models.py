from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class AppUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


# Cambiar los nombres de acceso inverso en las relaciones

AppUser._meta.get_field('groups').remote_field.related_name = 'appuser_set'
AppUser._meta.get_field('user_permissions').remote_field.related_name = 'appuser_set'

