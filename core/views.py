from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from core.models import Product


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product


class ProductCourseListView(ListView):
    template_name = 'product_courses.html'
    model = Product


class ProductTrainingListView(ListView):
    template_name = 'product_trainings.html'
    model = Product


class ProductServiceListView(ListView):
    template_name = 'product_services.html'
    model = Product


class GoToCartView(DetailView):
    pass


class ProductDetailView(DetailView):
    pass


class ProductCreateView(CreateView):
    pass


class ProductDeleteView(DeleteView):
    pass


class ContactView(DetailView):
    pass
