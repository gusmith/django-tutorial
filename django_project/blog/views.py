from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {"title": "Zen of Python", "posts": posts}
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")
