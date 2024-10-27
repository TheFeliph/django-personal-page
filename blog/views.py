from django.shortcuts import render

def post_view(request):
    return render(request, 'blog/templates/blog/index.html')  # Use o caminho correto para o template
