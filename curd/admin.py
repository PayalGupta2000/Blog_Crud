from django.contrib import admin
from .models import Product,Blog,Category


# Register your models here.
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','Title','Image','Description']


class BlogAdmin(admin.ModelAdmin):
    list_display=['user','Title','Image','Description']

    
