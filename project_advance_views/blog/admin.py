from django.contrib import admin        
from .models import BlogPost

my_model = [BlogPost]
admin.site.register(my_model)
