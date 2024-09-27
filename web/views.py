from django.shortcuts import render
from .models import Blog

# Create your views here.

def index(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')

def service(request):
    return render(request,'web/service.html')

def contact(request):
    return render(request,'web/contact.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {"is_blog": True,
               "blogs": blogs}
    return render(request, "web/blog.html", context)