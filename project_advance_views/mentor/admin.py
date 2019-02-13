from django.contrib import admin        # Default
from .models import Mentor

my_model = [Mentor]
admin.site.register(my_model)