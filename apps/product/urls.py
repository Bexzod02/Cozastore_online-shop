from django.urls import path
from .views import home_view, product_detail
app_name = 'products'

urlpatterns = [
    path('', home_view, name='index'),
    path('product-detail/<int:pk>/', product_detail, name='product-detail'),
    # path('modal/<int:pk>/', modal, name='modal')
]