from django.db import models
from django.contrib.auth.models import User
from apps.product.models import Category, Tag
# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=202)
    image = models.ImageField(upload_to = 'blog/')
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    story = models.TextField()
    

    def __str__(self):
        return self.name

class Comment(models.Model):
    article = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=202)
    email = models.EmailField()
    website = models.URLField(null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    