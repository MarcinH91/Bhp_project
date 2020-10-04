from django.urls import path

from core.views import ProductListView

app_name = 'core'

urlpatterns = [
    path('product/list', ProductListView.as_view())
]
