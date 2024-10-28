# blog/urls.py

from django.urls import path
from .views import post_view

urlpatterns = [
    path('', post_view, name='post_view'),  # URL básica para `post_view`
]
