from django.contrib import admin
from .models import Product, Cart, OrderItem, Order

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)

