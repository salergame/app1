from django_filters.rest_framework import FilterSet
from goods.models import Products


class ProductFilter(FilterSet):
    class Meta:
        model = Products
        fields ={
            'category_id': ['exact'],
            'price':['gt','lt'],
        }