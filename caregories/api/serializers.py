from rest_framework import serializers
from caregories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id",'title',"slug","published"]


