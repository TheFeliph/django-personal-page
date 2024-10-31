from django.urls import path
from .views import index  # use index em vez de post_view

urlpatterns = [
    path('', index, name='index'),  # rota raiz para a view `index`
]
