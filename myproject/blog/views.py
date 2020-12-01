from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog

# Create your views here.


def blog_detail(request, pk):

    blog = Blog.objects.filter(pk=pk)

    return render(request, 'front/blog_detail.html', {'blog': blog})
