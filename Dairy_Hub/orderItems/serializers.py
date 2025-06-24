from rest_framework import serializers

from orderItems.models import OrderItems

class OrderItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model=OrderItems
        fields="__all__"