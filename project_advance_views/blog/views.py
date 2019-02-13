from django.shortcuts import render, redirect
from .models import BlogPost 
from .forms import PostForm

# Create your views here.
def dbblog(request) :
    db_blog = BlogPost.objects.all()
    return render(request, 'blog/db-blog.html', {'db_blog': db_blog})

def input_post(request) :
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('db_blog')
    else :
        form = PostForm()
    return render(request, 'blog/post_blog.html', {'form' : form})

def blog_detail(request, blog_id) :
    blogs = BlogPost.objects.get(pk=blog_id)
    return render(request, 'Blog/blog_detail.html', {'blogs': blogs})