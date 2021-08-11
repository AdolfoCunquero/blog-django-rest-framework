from django.db.models import fields
from rest_framework import serializers
from posts.models import Posts
from users.api.serializers import UserSerializer
from caregories.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Posts
        fields = ["title","content","slug","miniature","created_at","published","user","category"]