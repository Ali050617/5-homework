from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentsSerializer
from .pagination import CommentsPagination


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    pagination_class = CommentsPagination

    # @action(detail=True, methods=['put'], url_path='approve')
    # def approve_comment(self, request, pk=None):
    #     comment = self.get_object()
    #     comment.is_approved = True
    #     comment.save()
    #     return Response({"id": comment.id, "is_approved": True, "approved_at": comment.created_at},
    #                     status=status.HTTP_200_OK)