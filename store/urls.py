from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListCreate, ProductDetails, StoreProductView, CustomAuthToken

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='ProductListCreate-api'),
    path('products/<int:pk>/', ProductDetails.as_view(), name='productdetails-api'),
    path('stores/<slug:slug>/products/', StoreProductView.as_view(),name='store-api'),
    path('login/', CustomAuthToken.as_view(), name='login-api'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)