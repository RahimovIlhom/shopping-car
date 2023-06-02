from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'url', 'username', 'brand', 'model', 'year', 'price', 'image', 'is_active', 'created_at']
