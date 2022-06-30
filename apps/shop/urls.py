from django.urls import path
from .views import shop_view,  add_cart, my_cart, \
    delete_item, plus_quantity, minus_quantitiy,add_wishlist,my_wishlist,checkout
app_name = 'shops'

urlpatterns = [
    path('', shop_view, name='shop'),
    path('add-wishlist/', add_wishlist, name='add-wishlist'),
    path('my-wishlist/', my_wishlist, name='my-wishlist'),
    path('add-cart/', add_cart, name='add-cart'),
    path('my-cart/', my_cart, name='my-cart'),
    path('plus-quantity/', plus_quantity, name='plus-quantity'),
    path('minus-quantity/', minus_quantitiy, name='minus-quantity'),
    path('delete-item/', delete_item, name='delete-item'),
    path('checkout/', checkout, name='checkout'),
]