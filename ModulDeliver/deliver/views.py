from django.db.models import Case, Value, When
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from deliver.models import Order, Box
from deliver.serializers import OrderSerializer, BoxSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
