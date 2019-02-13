from django.shortcuts import render
from .models import BlogPost 

# Create your views here.
def blog(request) :
    return render(request, 'blog/blog.html', {})

def dbblog(request) :
    blogs = BlogPost.objects.all()
    return render(request, 'blog/db-blog.html', {'blogs': blogs})

# def input_post(request) :
#     if request.method == "POST" :
#         form = PostForm(request.POST)
#         if form.is_valid() :
#             form.save()
#             return redirect('db_blog')
#     else :
#         form = PostForm()
#     return render(request, 'blog/post_blog.html', {'form' : form})