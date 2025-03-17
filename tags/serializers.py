from django.utils.text import slugify
from rest_framework import serializers
from .models import Tag


class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')
        read_only_fields = ('slug',)  # Make 'slug' read-only so it's not required in requests

    def create(self, validated_data):
        # Automatically generate slug if not provided
        validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)