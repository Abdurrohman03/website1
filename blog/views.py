from django.shortcuts import render, Http404
from .models import Blogs


def index(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog/index.html', {'object_list': blogs})


def detail(request, pk):
    if pk:
        obj = Blogs.objects.get(id=pk)
        return render(request, 'blog/detail.html', {'blog': obj})
    return Http404
