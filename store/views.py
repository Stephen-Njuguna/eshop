from django.shortcuts import render, redirect
from rest_framework.views import APIView
from  rest_framework import status
from rest_framework.response import Response
from .models import Vendor,Product,Store
from .serializers import StoreSerializer, VendorSerializer, ProductSerializer

# Create your views here.

#Defining API views for models
#Product
class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#Product details incase View

class ProductDetails(APIView):
    def get(self,request,pk):
        product = Product.objects.get(pk = pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def patch(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data =request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Store Details
class StoreProductView(APIView):
    def get(self, request, slug):
        store = Store.objects.get(slug=slug)
        products = Product.objects.filter(vendor=store.vendor)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
