from rest_framework import serializers
from .models import Product


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "slug", "description", "image", "price")
        
