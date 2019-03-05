from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'corey ms',
        'title': 'blog post',
        'content':'first post content',
        'date_posted': 'august 27, 2019'

    },
    {
            'author': 'lifey will',
            'title': 'blog post 2',
            'content':'second post content',
            'date_posted': 'sept 28, 2019'
    }
]
# Create your views here.
def home(request):
    context= {
        'posts': posts
    }
    return HttpResponse(request, 'blog/home.html', context)

def about(request):
    return HttpResponse(request, 'blog/about.html', {'title': 'about'})
