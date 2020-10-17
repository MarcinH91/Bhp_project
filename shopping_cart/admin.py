from django.contrib import admin
from shopping_cart.models import Order, OrderItem, Address

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Address)

