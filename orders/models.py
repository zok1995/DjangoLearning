from __future__ import unicode_literals

from django.db import models
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  #customize django admin
        return "Status: %s" % (self.name)

    class Meta: #Changing name of the model in the DB
        verbose_name = 'Status'
        verbose_name_plural = 'Orders statuses'

class Order(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=5, default=0)  # tpptal price for all orders
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  #customize django admin
        return "Order: %s  %s" % (self.id, self.status.name)

    class Meta: #Changing name of the model in the DB
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None) #link to order DB
    product = models.ForeignKey(Product, blank=True, null=True, default=None)

    price_per_item = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=5, default=0) #price*number
    number = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  #customize django admin
        return "Product: %s" % (self.product.name)

    class Meta: #Changing name of the model in the DB
        verbose_name = 'Product'
        verbose_name_plural = 'Products'