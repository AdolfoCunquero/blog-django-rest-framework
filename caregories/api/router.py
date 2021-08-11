from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from caregories.api.views import CategoryViewSet

router_categories = DefaultRouter()
router_categories.register(prefix="category", basename='category', viewset=CategoryViewSet)