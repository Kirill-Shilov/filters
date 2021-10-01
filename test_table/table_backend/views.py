from django.shortcuts import render
from .models import Table
from .serializers import TableSerializer
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from .filterset import TableFilter
from django_filters import rest_framework as filters


class TableList(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filterset_class = TableFilter
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['name', 'amount', 'distance']

