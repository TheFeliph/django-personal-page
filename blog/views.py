# blog/views.py

from django.shortcuts import render

def post_view(request):
    return render(request, 'blog/post.html')  # Ajuste o template conforme necessário
