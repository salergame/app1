from django.core.serializers import serialize
from django.shortcuts import render , get_object_or_404
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

from api.filters import ProductFilter
from carts.models import Cart, CartQueryset
from .serializer import CartSerializer, CategorySerializer, ProductSerializer
from goods.models import Categories, Products
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from api import serializer

# Create your views here.
class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
    
    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter] 
    filterset_class = ProductFilter                               
    search_fields = ['name','description']
    ordering_fields = ['price']
    pagination_class = PageNumberPagination
    
 
class CategoryViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class CartViewSet(CreateModelMixin, RetrieveModelMixin ,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer