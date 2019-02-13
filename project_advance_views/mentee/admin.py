from django.contrib import admin        # Default
from .models import Mentee

my_model = [Mentee]
admin.site.register(my_model)