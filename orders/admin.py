from django.contrib import admin
from .models import *

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields] #use itertor for every field name from DB
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields] #use itertor for every field name from DB

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields] #use itertor for every field name from DB

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)