from rest_framework import serializers
from rest_framework import viewsets
from .models import Category
from .pagination import CategoryPagination
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save()

