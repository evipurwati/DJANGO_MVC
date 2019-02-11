from django.contrib import admin        # Default
from .models import Direksi, Mentee, Mentor, Mata_Pelajaran, Challenge, Live_Code

my_model = [Direksi, Mentee, Mentor, Mata_Pelajaran, Challenge, Live_Code]
admin.site.register(my_model)