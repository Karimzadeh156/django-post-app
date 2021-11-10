from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home page'),
    path('about', views.about, name='about page'),
    path('arc/', views.ArticlesList, name='articles list'),
    path('artc/<arc_id>/', views.ArticleContinu, name='article continu'),
]
