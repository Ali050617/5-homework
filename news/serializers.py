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
        read_only_fields = ('created_at',)


class NewsSerializers(serializers.ModelSerializer):
    category = CategoryNewsSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, source='category'
    )
    tags = TagNewsSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, write_only=True, source='tags'
    )

    class Meta:
        model = New
        fields = ('id', 'title', 'slug', 'content', 'category', 'category_id',
                  'tags', 'tag_ids', 'image', 'is_published', 'created_at', 'updated_at')
        read_only_fields = ('slug', 'created_at', 'updated_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategoryNewsSerializer(instance.category).data
        representation['tags'] = TagNewsSerializer(instance.tags.all(), many=True).data
        return representation

    def to_internal_value(self, data):
        category_id = data.get('category_id')
        tag_ids = data.get('tag_ids', [])

        if category_id and not Category.objects.filter(id=category_id).exists():
            raise serializers.ValidationError({'category_id': 'Bunday kategoriya mavjud emas'})

        for tag_id in tag_ids:
            if not Tag.objects.filter(id=tag_id).exists():
                raise serializers.ValidationError({'tag_ids': f"Teg ID {tag_id} mavjud emas"})

        return super().to_internal_value(data)
