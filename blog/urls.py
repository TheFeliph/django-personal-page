<<<<<<< HEAD
"""
URL configuration for personal_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<<< HEAD:blog/urls.py
from django.urls import path
from .views import post_view

urlpatterns = [
    path('post/', post_view, name='post'),
========
# personal_page/urls.py

from django.contrib import admin
from django.urls import path, include  # Importando include para usar as URLs do app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Inclui as URLs do aplicativo blog
>>>>>>>> 25e1bf3 (Adiciona views de home e post):personal_page/urls.py
]

=======
# blog/urls.py

from django.urls import path
from .views import post_view, home_view  # Certifique-se de que home_view e post_view estão importados

urlpatterns = [
    path('', home_view, name='home'),       # URL raiz do blog (opcional)
    path('post/', post_view, name='post_view'),  # URL para a view de Post
]
>>>>>>> 25e1bf3 (Adiciona views de home e post)
