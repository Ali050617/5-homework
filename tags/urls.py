from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TagViewSet


router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tag_list')

urlpatterns = [
    path('', include(router.urls))
]
