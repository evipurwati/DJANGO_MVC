from django.shortcuts import render
from .models import Mentee

# Create your views here.
def mentee(request) :
    return render(request, 'mentee/mentee.html', {})

def dbmentee(request) :
    mentees = Mentee.objects.all()
    return render(request, 'mentee/db-mentee.html', {'mentees': mentees})