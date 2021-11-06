from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import article

def home(request):
    return render(request, 'articles/home.html')

def about(request):
    return render(request, 'articles/about.html')

def ArticlesList(request):
    global articles
    articles = article.objects.all().order_by('create_date')
    return render(request, 'articles/ArticlesList.html', {'articles':articles})

def ArticleContinu(request, arc_id):
    try:
        articles1 = get_object_or_404(article, pk=arc_id)
    except:
        return HttpResponse('صفحه مورد نظر پیدا نشد.')

    return render(request, 'articles/ArticleContinu.html', {'articles':articles1})
