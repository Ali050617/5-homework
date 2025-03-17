from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import NewsViewSet


router = DefaultRouter()
router.register(r'new', NewsViewSet, basename='list')

urlpatterns = [
   path('', include(router.urls)),
]