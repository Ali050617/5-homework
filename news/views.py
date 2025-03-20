from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import New
from .serializers import NewsSerializers, CommentNewsSerializer
from .pagination import NewsPagination, CommentNewsPagination
from comments.models import Comment


class NewsViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewsSerializers
    pagination_class = NewsPagination
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def comments(self, request, slug=None):
        news = self.get_object()
        comments = Comment.objects.filter(news=news).order_by('-created_at')
        paginator = CommentNewsPagination()
        paginated_comments = paginator.paginate_queryset(comments, request)
        serializer = CommentNewsSerializer(paginated_comments, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(detail=True, methods=['get', 'post'])
    def publish(self, request, slug=None):
        news = self.get_object()
        if not news.is_published:
            news.is_published = True
            news.published_at = timezone.now()
            news.save()

        return Response({
            "id": news.id,
            "title": news.title,
            "slug": news.slug,
            "is_published": news.is_published,
            "published_at": news.published_at,
        }, status=status.HTTP_200_OK)
