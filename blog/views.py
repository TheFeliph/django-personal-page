from django.http import HttpResponse

<<<<<<< HEAD
=======
def home_view(request):
    return HttpResponse("Welcome to the Home Page!")

>>>>>>> 25e1bf3 (Adiciona views de home e post)
def post_view(request):
    return HttpResponse("Hello World")
