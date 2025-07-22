from rest_framework import serializers
from .models import Vendor, Product,Store

# Create serializers here 
#Vendor serializer

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

#Product serializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'

# Store serializer

class StoreSerializer(serializers.ModelSerializer):
    class meta:
        model = Store
        fields = '__all__'