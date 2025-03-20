from rest_framework import serializers
from .models import Comment
from news.models import New


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ["id", "title", "slug"]


class CommentApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'is_approved', 'approved_at')
        read_only_fields = ('id', 'approved_at')


class CommentsSerializer(serializers.ModelSerializer):
    news = NewsSerializer(read_only=True)
    news_id = serializers.PrimaryKeyRelatedField(
        queryset=New.objects.all(), write_only=True, source="news"
    )

    class Meta:
        model = Comment
        fields = ('id', 'news', 'news_id', 'author_name', 'author_email', 'content', 'is_approved', 'created_at')
        read_only_fields = ('is_approved', 'created_at')
