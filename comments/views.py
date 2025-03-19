from rest_framework import viewsets
from .models import Comment
from .serializers import CommentsSerializer
from .pagination import CommentsPagination


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    pagination_class = CommentsPagination

