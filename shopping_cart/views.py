from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from shopping_cart.models import Order


class AddToCartView(ListView):
    template_name = 'cart.html'
    model = Order


class RemoveFromCartView(ListView):
    template_name = 'cart.html'
    model = Order


class GoToCartView(ListView):
    template_name = 'cart.html'
    model = Order
