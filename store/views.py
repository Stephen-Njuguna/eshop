from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Vendor,Product,Store
from .serializers import StoreSerializer, VendorSerializer, ProductSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.

#Defining API views for models
#Product
class ProductListCreate(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
#Product details incase View

class ProductDetails(APIView):
    permission_classes = [IsAuthenticated]
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

#Getting user token for auth 
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
        })

