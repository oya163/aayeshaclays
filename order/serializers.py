from product.models import Product
from django.db.models import fields
from rest_framework import serializers
from .models import Order, OrderItem, ShippingAddress
from product.serializers import ProductSerializer

class MyOrderItemSerializer(serializers.ModelSerializer): 
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
      model = ShippingAddress
      fields = (
          "address1",
          "address2",
          "zip_code",
          "city",
          "country",
      )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)
    address = ShippingAddressSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "paid_amount",
            "stripe_token",
            "items",
            "address",
        )

class OrderItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    address = ShippingAddressSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "stripe_token",
            "items",
            "address",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        address_data = validated_data.pop('address')
        address = ShippingAddress.objects.create(**address_data)

        order = Order.objects.create(**validated_data, address=address)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order