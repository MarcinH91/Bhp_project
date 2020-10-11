from django.views.generic import ListView

from core.views import ProductListView


class IndexView(ProductListView):
    title = 'Witamy w firmie Szkolenia Bhp!'
    template_name = 'index.html'
