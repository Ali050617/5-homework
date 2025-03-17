from rest_framework import viewsets
from .models import New
from .serializers import NewsSerializers
from .pagination import NewsPagination


class NewsViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewsSerializers
    pagination_class = NewsPagination
    lookup_field = 'slug'
