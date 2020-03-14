from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# posts = [
#     {
#         'title': 'Blog post 1',
#         'author': 'Haris',
#         'content': 'i am designing blog in django with awesome features'
#     },
#     {
#         'title': 'Blog post 2',
#         'author': 'Haris',
#         'content': 'i am designing blog in django with awesome features'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
