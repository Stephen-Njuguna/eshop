from django.contrib import admin
from .models import Vendor, Product, Store

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'created_at', 'location']
    search_fields = ['vendor']

# Vendor admin settings 

class AdminVendor(admin.ModelAdmin):
    list_display = ['user','phone']
    search_fields = ['user']
    list_filter  = ['joined_at']

# Registering site to admin page

admin.site.register(Vendor, AdminVendor)
admin.site.register(Product)
admin.site.register(Store, StoreAdmin)
