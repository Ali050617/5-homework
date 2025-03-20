from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils.timezone import now
from rest_framework.decorators import action
from .models import Comment
from .serializers import CommentsSerializer, CommentApproveSerializer
from .pagination import CommentsPagination


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    pagination_class = CommentsPagination

    @action(detail=True, methods=['get', 'put'], url_path='approve')
    def approve(self, request, pk=None):
        comment = self.get_object()
        comment.is_approved = True
        comment.approved_at = now()
        comment.save()

        serializer = CommentApproveSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)