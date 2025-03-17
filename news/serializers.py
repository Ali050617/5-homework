from rest_framework import serializers
from .models import New


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'slug', 'content', 'category',
                  'tags', 'image', 'is_published', 'created_at', 'updated_at')
        read_only_fields = ('slug', 'created_at', 'updated_at')

