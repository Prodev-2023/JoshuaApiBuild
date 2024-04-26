from django.urls import path
from blog import views

# my urls pattern here

urlpatterns = [
    path('', views.home, name='home-page'),
     path('about/', views.about, name='about-page'),
]
