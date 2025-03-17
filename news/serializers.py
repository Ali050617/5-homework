from rest_framework import serializers
from .models import New
from categories.models import Category
from tags.models import Tag
from comments.models import Comment


class CategoryNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class TagNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')


class CommentNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'is_approved', 'created_at')
        read_only_fields = ('created_at', )


class NewsSerializers(serializers.ModelSerializer):
    category = CategoryNewsSerializer(read_only=True)
    tags = TagNewsSerializer(many=True, read_only=True)

    class Meta:
        model = New
        fields = ('id', 'title', 'slug', 'content', 'category',
                  'tags', 'image', 'is_published', 'created_at', 'updated_at')
        read_only_fields = ('slug', 'created_at', 'updated_at')

