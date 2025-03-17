from rest_framework import serializers
from .models import Comment
from news.models import New


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ["id", "title", "slug"]


class CommentsSerializer(serializers.ModelSerializer):
    news = NewsSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'news', 'author_name', 'author_email', 'content', 'is_approved', 'created_at')
        read_only_fields = ('is_approved', 'created_at')

