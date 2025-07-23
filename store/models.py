from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

#Creating of vendors model
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(blank=False, default="vendor_banner.avif", upload_to='banners/')
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.store_name
    
# Product Model

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products_images/', blank=True)
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# Store model 

class Store(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    location = models.TextField(blank=False)

    def __str__(self):
        return self.vendor.store_name
    
    from django.utils.text import slugify

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.vendor.store_name)
    super().save(*args, **kwargs)

    def get_products(self):
        return Product.objects.filter(vendor = self.vendor)
