from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateTimeField
from django.db.models import ImageField
from django.utils import timezone

from django.db import models as models

class Mentee(models.Model) :
    foto = models.ImageField()
    nama_lengkap = models.CharField(max_length = 255)
    description = models.TextField(max_length = 600)

    def __str__(self) :
        return self.nama_lengkap