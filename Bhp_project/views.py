from django.views.generic import ListView

from core.views import ProductListView


class IndexView(ProductListView):
    title = 'Welcome to Django Movies!'
    template_name = 'index.html'
