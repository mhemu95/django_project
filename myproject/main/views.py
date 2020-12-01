from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from blog.models import Blog


# Create your views here.

def home(request):

    site = Main.objects.get(pk=1)
    blog = Blog.objects.all()

    return render(request, 'front/home.html', {'site': site, 'blog': blog})


def archive(request):

    site = Main.objects.get(pk=1)

    return render(request, 'front/archive.html', {'site': site})
