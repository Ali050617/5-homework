from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'author_name', 'author_email', 'content', 'is_approved')
    search_fields = ('news', 'author_name', 'content')
    list_filter = ('author_name',)
