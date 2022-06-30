from distutils.command.upload import upload
from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=202)

    @property
    def get_normalize_title(self):
        return self.title.replace(' ', '')

    def __str__(self):
        return self.title

class Color(models.Model):
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.color

class Tag(models.Model):
    tags = models.CharField(max_length=202)

    def __str__(self):
        return self.tags

class Size(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class Banner(models.Model):
    banner = models.ImageField(upload_to = 'banners')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

TYPE = (
        (0, 'Men'),
        (1, 'Women'),
        (2, 'Accessories'),
        (3, 'Bags'),
        (4, 'Watches'),
        (5, 'Shoes'),
    )
class Typecart(models.Model):
    image = models.ImageField(upload_to = 'type')
    type = models.IntegerField(choices=TYPE)
    seasion = models.CharField(max_length=200)

    @property
    def get_normalize_title(self):
        return self.get_type_display

    def __str__(self):
        return self.seasion
    

class Product(models.Model):
    name = models.CharField(max_length=202)
    price = models.FloatField()
    content = models.TextField()
    describtion = models.TextField()
    type = models.IntegerField(choices=TYPE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    size = models.ManyToManyField(Size)
    tag = models.ManyToManyField(Tag)
    color = models.ManyToManyField(Color,)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    mid_rate = models.FloatField(default=0)


    def __str__(self):
        return f'{self.id} | {self.name}'
    
    @property
    def get_mid_rate(self):
        rates = self.rate_set.all()
        mid = 0
        try:
            mid = sum([i.rate for i in rates])/rates.count()
        except ZeroDivisionError:
            pass
        self.mid_rate = mid
        self.save()
        return mid

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product/')

    def __str__(self):
        return f'image of {self.product}'

class Rate(models.Model):
    RATE = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL),
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATE, default=0)

    def __str__(self):
        return f'rate of {self.user}'

class Addition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.CharField(max_length=20)
    demismession = models.CharField(max_length=20)
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.product.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()
    names = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatar/', null=True)

    def __str__(self):
        return self.names
    
    


    

    
    







    
    
