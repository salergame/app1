from re import T
from rest_framework import serializers
from carts.models import Cart
from goods.models import Categories, Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','name','slug']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["id","name","description","category","slug","price",'discount','sell_price',"quantity" ]

    category = CategorySerializer()



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["user","product","quantity",]


