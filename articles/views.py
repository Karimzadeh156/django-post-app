from django.shortcuts import render
from django.shortcuts import HttpResponse
from .import models

def home(request):
    return render(request, 'articles/home.html')

def about(request):
    return render(request, 'articles/about.html')

def ArticlesList(request):
    global articles
    articles = models.article.objects.all().order_by('create_date')
    return render(request, 'articles/ArticlesList.html', {'articles':articles})

def ArticleContinu(request, arc_id):
    articles1 = models.article.objects.get(pk=arc_id)
    return render(request, 'articles/ArticleContinu.html', {'articles':articles1})
