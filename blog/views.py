from django.shortcuts import render
from .models import Blog

def BlogListView(request) :
    blogs = Blog.objects.all();
    
    context = {
        "blogs" : blogs
    }
    
    return render(request , "home.html" ,context=context )
