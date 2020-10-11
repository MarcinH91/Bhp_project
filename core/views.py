from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from core.models import Product


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product
    success_url = reverse_lazy('core:product_list')




class ProductCourseListView(ListView):
    template_name = 'product_courses.html'
    model = Product
    success_url = reverse_lazy('core:product_courses')


class ProductTrainingListView(ListView):
    template_name = 'product_trainings.html'
    model = Product
    success_url = reverse_lazy('core:product_trainings')


class ProductServiceListView(ListView):
    template_name = 'product_services.html'
    model = Product
    success_url = reverse_lazy('core:product_services')


class GoToCartView(DetailView):
    pass


class ProductDetailView(DetailView):
    template_name = 'product_details.html'
    model = Product
    success_url = reverse_lazy('core:product_details')


class ProductCreateView(CreateView):
    pass


class ProductDeleteView(DeleteView):
    pass



