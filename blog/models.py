from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(unique=True)  # Campo para o slug, deve ser único
    created = models.DateTimeField(auto_now_add=True)  # Campo de data/hora de criação
    updated = models.DateTimeField(auto_now=True)  # Campo de data/hora de atualização
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')  # Campo de status

    def __str__(self):
        return self.title
