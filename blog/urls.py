from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]