from rest_framework import viewsets
from .models import Tag
from .serializers import TagsSerializers
from .pagination import TagsPagination


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializers
    pagination_class = TagsPagination
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save()