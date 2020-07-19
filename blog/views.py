from django.shortcuts import render, get_object_or_404
from .models import BlogTable, AuthorTable

app_name = 'blog'


def home_view(request):
    return render(request, 'blog/home.html')


def blog_view(request):
    obj = BlogTable.objects.all()
    return render(request, 'blog/blog.html', {'obj': obj})


def author_view(request, id):
    obj1 = get_object_or_404(AuthorTable, id=id)
    return render(request, 'blog/author.html', {'obj1': obj1})
