from django.urls import path

from core.views import ProductListView, ProductCourseListView, ProductTrainingListView, ProductServiceListView

app_name = 'core'

urlpatterns = [
    path('product/list', ProductListView.as_view(), name='product_list'),
    path('product/list/courses', ProductCourseListView.as_view(), name='product_courses'),
    path('product/list/trainings', ProductTrainingListView.as_view(), name='product_trainings'),
    path('product/list/services', ProductServiceListView.as_view(), name='product_services'),
]
