from django.shortcuts import render, get_object_or_404,redirect
from apps.product.models import Product, Category, Tag
from .forms import CommentForm
from .models import Comment,Blog
# Create your views here.

def blog_view(request):
    comment = Comment.objects.all()
    products = Blog.objects.all()
    blogs = Product.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)
    if tag:
        products = products.filter(tag__tags__iexact=tag)
    if cat:
        products = products.filter(category__title__iexact=cat)
    ctx = {
        'products':products,
        'blogs':blogs,
        'tags':tags,
        'categories':categories,
        'comments':comment
    }
    return render(request, 'blog.html', ctx)

def blog_detail(request, pk):
    products = get_object_or_404(Blog, id = pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    blogs = Product.objects.all()[:3]
    comments = Comment.objects.filter(id = pk)
    form=CommentForm()
    if request.method=="POST":
        form=CommentForm(request.POST or None)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.products=products
            comment.save()
            return redirect('/blog/')
    ctx = {
        'products':products,
        'categories':categories,
        'tags':tags,
        'blogs':blogs,
        'form':form,
        'comments':comments
    }
    return render(request, 'blog-detail.html', ctx)




