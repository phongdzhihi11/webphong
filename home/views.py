from django.shortcuts import render
from django.views import View
from home.models import Post


# Create your views here.


class Index(View):
    def get(self, request):
        sql = "SELECT * From home_post"
        post = Post.objects.raw(sql)
        context = {
            'post': post
        }
        return render(request, 'home/index.html', context)

class Movies(View):
    def get(self, request):
        sql = "SELECT * From home_post"
        post = Post.objects.raw(sql)
        context = {
            'post': post
        }
        return render(request, 'home/movie.html', context)

class Videogame(View):
    def get(self, request):
        sql = "SELECT * From home_post"
        post = Post.objects.raw(sql)
        context = {
            'post': post
        }
        return render(request, 'home/video_game.html', context)

class Music(View):
    def get(self, request):
        sql = "SELECT * From home_post"
        post = Post.objects.raw(sql)
        context = {
            'post': post
        }
        return render(request, 'home/music.html', context)
