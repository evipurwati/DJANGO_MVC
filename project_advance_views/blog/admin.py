from django.contrib import admin        # Default
from .models import BlogPost

my_model = [BlogPost]
admin.site.register(my_model)
