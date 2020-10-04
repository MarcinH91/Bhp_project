from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView


class GoToCartView(DetailView):
    pass


class ProductListView(ListView):
    pass


class ProductDetailView(DetailView):
    pass


class ProductCreateView(CreateView):
    pass


class ProductDeleteView(DeleteView):
    pass


class ContactView(DetailView):
    pass
