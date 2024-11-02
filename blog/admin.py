from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created', 'updated')
    list_filter = ('status', 'created')
    ordering = ('status', 'created')
    date_hierarchy = 'created'

admin.site.register(Post, PostAdmin)
