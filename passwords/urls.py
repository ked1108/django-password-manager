from django.urls import path

from . import views

urlpatterns = [
        path('', views.home, name="home"),
        path('home/', views.home, name="home"),
        path('views/', views.pwrds, name='passwords'),
        path('create/', views.create, name='create'),
        path('change/', views.change, name='change'),
        path('delete/', views.delete, name='delete'),
        path('search/', views.search, name='search')
        ]
