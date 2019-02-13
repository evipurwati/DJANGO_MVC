from django.shortcuts import render
from .models import Mentor

# Create your views here.
def mentor(request) :
    return render(request, 'mentor/mentor.html', {})

def dbmentor(request) :
    mentors = Mentor.objects.all()
    return render(request, 'mentor/db-mentor.html', {'mentors': mentors})