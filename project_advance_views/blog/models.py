from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateTimeField
from django.db.models import ImageField
from django.utils import timezone

from django.db import models as models

class BlogPost(models.Model) :
    foto = models.ImageField(upload_to="blog/static/images")
    created = models.DateTimeField(default = timezone.now)
    comments = models.CharField(max_length = 5)
    title = models.TextField(max_length = 100)
    content = models.TextField(max_length = 600)

    def __str__(self) :
        return self.title

