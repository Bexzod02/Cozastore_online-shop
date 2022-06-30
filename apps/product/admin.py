from django.contrib import admin
from .models import Product, Rate, Review, \
     Category, Color, Tag, Addition, Size, Banner, ProductImage, Typecart
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class RateInline(admin.TabularInline):
    model = Rate
    extra = 1
class AdditionLine(admin.TabularInline):
    model = Addition
    extra = 1

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tags', )

class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size')

class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color')

class Productadmin(admin.ModelAdmin):
    inlines = [ProductImageInline, RateInline, AdditionLine]
    filter_horizontal = ('tag', 'size', 'color',)

admin.site.register(Category)
admin.site.register(Product, Productadmin)   
admin.site.register(Color, ColorAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Banner)
admin.site.register(Typecart)
admin.site.register(Addition)
admin.site.register(Review)
