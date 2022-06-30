from .forms import OrderForm
from django.http import JsonResponse
from django.shortcuts import render,redirect
from apps.product.models import Product, Typecart, Category, Color, Tag
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.shop.models import Cart, CartItem, Wishlist


# Create your views here.


def shop_view(request):
    typecart = Typecart.objects.all()[:3]
    products = Product.objects.all()
    colors = Color.objects.all()
    tags = Tag.objects.all()
    color = request.GET.get('color')
    tag = request.GET.get('tag')
    price = request.GET.get('price')
    if price:
        a = price.index('-')
        lst = [int(price[:a]), int(price[a + 1:])]
        products = products.filter(price__range=(lst[0], lst[1]))
    if tag:
        products = products.filter(tag__tags__iexact=tag)
    if color:
        products = products.filter(color__color__iexact=color)
    ctx = {
        'products': products,
        'typecart': typecart,
        'colors': colors,
        'tags': tags
    }
    return render(request, 'product.html', ctx)

def add_wishlist(request):
    pid = request.GET.get('_pid')
    product = Product.objects.get(id = pid)
    wishlist_count = Wishlist.objects.filter(user = request.user, product = product).count()
    if wishlist_count < 1:
        Wishlist.objects.create(user = request.user, product=product)
        data = {
            'success' : True,
            'product' : product.name
        }
    else :
        Wishlist.objects.get(user = request.user, product = product).delete()
        data = {
            'success' : False, 'product' : product.name
        }
    return JsonResponse(data)

def my_wishlist(request):
    my_wishlist = Wishlist.objects.filter(user = request.user)
    products = Product.objects.all()
    typecart = Typecart.objects.all()[:3]
    colors = Color.objects.all()
    tags = Tag.objects.all()
    color = request.GET.get('color')
    tag = request.GET.get('tag')
    price = request.GET.get('price')
    if price:
        a = price.index('-')
        lst = [int(price[:a]), int(price[a + 1:])]
        products = products.filter(price__range=(lst[0], lst[1]))
    if tag:
        products = products.filter(tag__tags__iexact=tag)
    if color:
        products = products.filter(color__color__iexact=color)
    ctx = {
        'porducts' : products,
        'my_wishlist':my_wishlist,
        'typecart': typecart,
        'colors': colors,
        'tags': tags
    }
    return render(request, 'wishlist.html', ctx)

def add_cart(request):
    pid = request.GET.get('_pid')
    user = request.user
    product = Product.objects.get(id=pid)
    my_cart, new_cart = Cart.objects.get_or_create(cilent=user, is_ordered=False)
    cart_products = []
    for i in my_cart.cart_items.all():
        cart_products.append(i.product.id)

    print(cart_products)
    data = None
    if my_cart:
        if product.id in cart_products:
            ci = CartItem.objects.get(product=product, cart=my_cart)
            ci.quantitiy += 1
            ci.save()
        else:
            CartItem.objects.create(product=product, cart=my_cart)
        data = {
            'success': True,
            'product': product.name
        }
    if new_cart:
        CartItem.objects.create(product=product, cart=new_cart)
        data = {
            'success': True,
            'product': product.name
        }
    return JsonResponse(data, status=201)


def my_cart(request):
    cart, cart = Cart.objects.get_or_create(cilent=request.user, is_ordered=False)
    ctx = {
        'cart': cart
    }
    return render(request, 'shoping-cart.html', ctx)

def plus_quantity(request):
    ciid = request.GET.get('_ciid')
    cart_item = CartItem.objects.get(id=ciid)
    cart_item.quantitiy += 1
    cart_item.save()
    data = { 'success':True }
    return JsonResponse(data, status = 201)

def minus_quantitiy(request):
    ciid = request.GET.get('_ciid')
    cart_item  =CartItem.objects.get(id = ciid)
    if cart_item.quantitiy > 1:
        cart_item.quantitiy -= 1
        cart_item.save()
        data = { 'success':True }
    else :
        cart_item.delete()
        data = {'success':True, 'deleted':True}
    
    return JsonResponse(data, status = 201)

def delete_item(request):
    ciid = request.GET.get('_ciid')
    cart_item = CartItem.objects.get(id = ciid)
    cart_item.delete()
    data = {'success':True, 'deleted':True}
    
    return JsonResponse(data, status = 201)

def checkout(request):
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    print(cart.is_ordered)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.cart = cart
            order.client = request.user
            order.save()
            cart.is_ordered = True
            cart.save()
            messages.success(request, 'Muvafaqiyatli yakunlandi!!!')
    ctx = {
        'form': form,
        'cart': cart,
    }
    return render(request, 'chekout.html', ctx)


