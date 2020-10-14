from django.urls import path

from shopping_cart.views import (
    RemoveFromCartView,
    OrderSummaryView,
    add_to_cart

)

app_name = 'shopping_cart'

urlpatterns = [
    path('add/<slug>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<pk>', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart', OrderSummaryView.as_view(), name='cart')
]
