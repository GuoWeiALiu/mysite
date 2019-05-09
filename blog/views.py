from django.shortcuts import render

# Create your views here.
from blog.models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs':blogs})
