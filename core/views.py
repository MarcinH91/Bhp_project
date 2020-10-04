from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from core.models import Product


class GoToCartView(DetailView):
    pass


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product


class ProductDetailView(DetailView):
    pass


class ProductCreateView(CreateView):
    pass


class ProductDeleteView(DeleteView):
    pass


class ContactView(DetailView):
    pass
