# Import the admin module
from django.contrib import admin

# Import your models
from .models import Client, ClientType, Product, Order

# Register your models to make them available in the admin interface
admin.site.register(Client)
admin.site.register(ClientType)
admin.site.register(Product)
admin.site.register(Order)
