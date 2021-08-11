from rest_framework.viewsets import ModelViewSet
from caregories.models import Category
from caregories.api.serializers import CategorySerializer
from caregories.api.permissions import isAdminOrReadAll
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(ModelViewSet):
    permission_classes = [isAdminOrReadAll]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    queryset = Category.objects.filter(published=True)
    lookup_field = "slug"
    
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["published"]
    


