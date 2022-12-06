from django.shortcuts import render, Http404
from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'article/index.html', {'object_list': articles})


def detail(request, pk):
    if pk:
        obj = Article.objects.get(id=pk)
        return render(request, 'article/detail.html', {'article': obj})
    return Http404
