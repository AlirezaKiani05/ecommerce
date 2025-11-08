from rest_framework import serializers
from .models import Category, Product, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'parent')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id','name')
        
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand=BrandSerializer()
    
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'brand')