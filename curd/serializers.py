from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    category_name=CategorySerializer(many=False)
    class Meta: 
        model=Product
        fields="__all__"




class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"
 