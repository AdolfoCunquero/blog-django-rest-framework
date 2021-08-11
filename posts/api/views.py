from rest_framework.viewsets import ModelViewSet
from posts.api.serializers import PostSerializer
from posts.models import Posts
from posts.api.permissions import isAdminOrReadAll
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    permission_classes = [isAdminOrReadAll]
    serializer_class = PostSerializer
    queryset = Posts.objects.filter(published=True)
    lookup_field = "slug"

    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ["category"]
    filterset_fields = ["category__slug"]
