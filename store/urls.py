from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListCreate, ProductDetail, StoreProductView

urlpatterns = [
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('stores/<slug:slug>/products/', StoreProductView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)