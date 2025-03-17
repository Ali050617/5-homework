from rest_framework import serializers
from .models import Comment


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'news', 'author_name', 'author_email', 'content')
        read_only_fields = ('is_approved', 'created_at')

