import uuid
from venv import create
from django.db import models
from apps.product.models import Product, Typecart
from django.contrib.auth.models import User
# Create your models here.

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f' wishlist of {self.user.username} (id: {self.id})'

class Cart(models.Model):
    cilent = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'cart of {self.cilent}'

    @property
    def get_cart_items(self):
        cart_items = self.cart_items.all()
        total = sum([item.quantitiy for item in cart_items])
        return total

    @property
    def get_cart_total(self):
        cart_items = self.cart_items.all()
        total = sum([item.get_total for item in cart_items])
        return total

    def __str__(self):
        return f'order of {self.cilent}'
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_items')
    quantitiy = models.IntegerField(null=True, default = 1)
    # total = models.FloatField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def get_total(self):
        return self.quantitiy * self.product.price

class Order(models.Model):
    STATUS = (
        (0, 'NEW'),
        (1, 'PROCESS'),
        (2, 'DELIVRED'),
        (3, 'CANCELLED')
    )
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cilent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    note = models.CharField(max_length=200, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'order in by {self.cilent} id: {self.transaction_id}'

    