from django.contrib import admin
from .models import New


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'category',
                    'image', 'is_published', 'created_at', 'updated_at')
    search_fields = ('slug', 'tags', 'category')
    list_filter = ('title', 'content', 'created_at')