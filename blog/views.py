from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
    template_name = 'home.html'
    return render(request, template_name)


def Blog(request):
    posts = BlogPost.objects.filter(status = 'published')
    template_name = 'Blog/blog.html'
    context = {'posts': posts}
    return render(request, template_name, context)