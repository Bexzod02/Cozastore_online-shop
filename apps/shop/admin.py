from django.contrib import admin
from .models import Order,Cart,CartItem,Wishlist


class CartItemList(admin.TabularInline):
    model = CartItem
    extra = 1

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemList]


admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(Cart, CartAdmin)

