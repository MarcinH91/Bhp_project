from django.urls import path

from shopping_cart.views import (
    RemoveFromCartView,
    GoToCartView,
    add_to_cart

)

app_name = 'shopping_cart'

urlpatterns = [
    path('add/<pk>', add_to_cart, name='add_to_cart'),
    # path('add_to_cart/<pk>', AddToCartView.as_view(), name='add_to_cart'),
    path('remove_from_cart/<pk>', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart', GoToCartView.as_view(), name='cart')
]
