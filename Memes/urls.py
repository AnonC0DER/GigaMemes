from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.MemesViews, name='Home'),
    path('meme/<str:pk>/', views.SingleMemeViews, name='single-meme'),
]