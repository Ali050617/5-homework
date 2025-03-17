from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class NewsPagination(PageNumberPagination):
    page_size = 10


class CommentNewsPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "results": data
        })
