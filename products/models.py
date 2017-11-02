from __future__ import unicode_literals

from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):  # customize django admin
        return "%s" % (self.name)

    class Meta:  # Changing name of the model in the DB
        verbose_name = 'Product category'
        verbose_name_plural = 'Products category'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  #customize django admin
        return "%s, %s" % (self.price, self.name)

    class Meta: #Changing name of the model in the DB
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='./products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  #customize django admin
        return "%s" % (self.id)

    class Meta: #Changing name of the model in the DB
        verbose_name = 'Image'
        verbose_name_plural = 'Images'