from django.urls import path
from home import views

# from home import views as home

app_name = 'home'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('movies/', views.Movies.as_view(), name='movies'),
    path('videogame/', views.Videogame.as_view(), name='videogame'),
    path('music/', views.Music.as_view(), name='music'),
]
