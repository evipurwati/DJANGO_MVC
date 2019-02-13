from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm) :
    class Meta :
        model = BlogPost
        fields = ('foto', 'created', 'comments', 'title', 'content')
