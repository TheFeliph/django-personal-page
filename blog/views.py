# blog/views.py

from django.shortcuts import render
from .models import Post  # Supondo que você tenha um modelo Post

def index(request):
    posts = Post.objects.all()  # Obtenha todos os posts do Admin
    return render(request, 'blog/index.html', {'posts': posts})  # Use 'blog/index.html'
