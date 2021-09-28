from django.db.models import fields
from rest_framework import serializers

from .models import Category, Color, Product, Collection, ImageModel

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = (
            "id",
            "name",
            "product",
            "get_image",
            "date_added",
            "default",
        )

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, source="product_image")
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "color",
            "collection",
            "description",
            "price",
            "images"
        )

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            "id",
            "name",
            "get_absolute_url"
        )

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = (
            "id",
            "name",
            "get_absolute_url"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )