from rest_framework.viewsets import ModelViewSet
from coments.models import Comment
from coments.api.serializers import CommentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from coments.api.permissions import isOwnerOrReadAndCreateOnly  

class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [isOwnerOrReadAndCreateOnly]
    queryset = Comment.objects.all()
    
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ["-created_at"]
    filterset_fields = ["post"]
