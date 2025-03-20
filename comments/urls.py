from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CommentsViewSet

router = DefaultRouter()
router.register(r'comments', CommentsViewSet, basename='comments_list')

urlpatterns = [
    path('', include(router.urls)),
    path('comments/<int:pk>/approve/', CommentsViewSet.as_view({'put': 'approve'}), name='comment_approve'),
]
