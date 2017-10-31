from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields] #use itertor for every field name from DB
    inlines = [ProductImageInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields] #use itertor for every field name from DB

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)