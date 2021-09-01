from django.db.models import fields
from rest_framework import serializers

from .models import Category, Color, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "color",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            "id",
            "name",
            "get_absolute_url"
        )