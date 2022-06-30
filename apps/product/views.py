from concurrent.futures import process
from django.shortcuts import redirect, render, get_object_or_404
from .models import Color, Product, Category, Banner, Size, Tag, Typecart, Addition, Review
from .forms import ReviewForm
# Create your views here.
def home_view(request):
    categories = Category.objects.all().order_by("-id")
    banners = Banner.objects.all()
    products = Product.objects.all()
    typecart = Typecart.objects.all()[:3]
    search = request.GET.get('search')
    colors = Color.objects.all()
    tags = Tag.objects.all()
    price = request.GET.get('price')
    color = request.GET.get('color')
    print( 'color' , color)
    if price:
        a = price.index('-')
        lst = [int(price[:a]), int(price[a + 1: ])]
        products = products.filter(price__range=(lst[0], lst[1]))
    if search:
        products = products.filter(name__icontains=search)
    if color:
        products = products.filter(color__color__exact=color)
    ctx={
        'categories':categories,
        'banners':banners,
        'products':products,
        'typecart':typecart,
        'colors':colors,
        'tags':tags
    }
    return render(request, 'index.html', ctx)

def product_detail(request, pk):
    products = Product.objects.get(id=pk)
    productss = Product.objects.all()
    objects = Addition.objects.get(product__id = pk)
    size = Size.objects.all()
    color = Color.objects.all()
    form = ReviewForm(request.POST or None, request.FILES)
    if form.is_valid():
        com = form.save(commit=False)
        com.author = request.user
        com.product = products
        com.save()
        return redirect('.')
    ctx  = {
        'products':products,
        'sizes':size,
        'productss':productss,
        'colors':color,
        'form':form,
        'objects':objects,
    }
    return render(request, 'product-detail.html', ctx)