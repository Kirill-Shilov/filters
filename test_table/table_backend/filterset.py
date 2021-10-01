from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Table


class TableFilter(filters.FilterSet):

    class Meta:
        model = Table
        fields = {
                'name': ['exact', 'contains', 'gt', 'lt'],
                'amount': ['exact', 'contains', 'gt', 'lt'],
                'distance': ['exact', 'contains', 'gt', 'lt']
                }

