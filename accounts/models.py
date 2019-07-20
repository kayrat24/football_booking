from authtools.models import AbstractEmailUser, AbstractNamedUser
from django.db import models

class User(AbstractEmailUser):
    full_name = models.CharField(('name'), max_length=255, blank=True)

    def __str__(self):
        return '{name} <{email}>'.format(
            name = self.full_name, email = self.email,
        )

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name


# Create your models here.
