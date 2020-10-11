from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.decorators.http import require_http_methods

from shopping_cart.models import Order
from core.models import Product


class AddToCartView(ListView):
    model = Product


@require_http_methods(["POST"])
def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)
    order = Order.objects.get(id=1)
    order.items.add(product)
    return redirect(request.path_info)


class RemoveFromCartView(ListView):
    template_name = 'cart.html'
    model = Order


class GoToCartView(ListView):
    template_name = 'cart.html'
    model = Order
