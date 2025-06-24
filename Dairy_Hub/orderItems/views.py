from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from orderItems.models import OrderItems

from .serializers import OrderItemsSerializers

class OrderItemsViewSet(viewsets.ModelViewSet):

    queryset=OrderItems.objects.all()

    serializer_class=OrderItemsSerializers
