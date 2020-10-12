from django.contrib import admin
from shopping_cart.models import Order, OrderProduct

# admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(OrderProduct)
