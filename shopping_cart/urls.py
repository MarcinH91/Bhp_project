from django.urls import path

from shopping_cart.views import (
    OrderSummaryView,
    add_to_cart,
    remove_from_cart

)

app_name = 'shopping_cart'

urlpatterns = [
    path('add/<slug>', add_to_cart, name='add_to_cart'),
    path('cart', OrderSummaryView.as_view(), name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove_from_cart')
]
