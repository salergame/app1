from re import T
from rest_framework import serializers
from carts.models import Cart
from goods.models import Categories, Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','name','slug']

class ProductsSerializer():
    class Meta:
        model = Products
        fields = "__all__"

    category = CategorySerializer()