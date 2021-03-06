from django.shortcuts import render
from .forms import SubscriberForm
import time
from products.models import *
# Create your views here.


def landing(request):
    name = "Oleksandr"
    currentDay = time.strftime("%H:%M:%S")

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid(): #Django use get as default method
        print(request.POST)
        data  = form.cleaned_data
        # print(data["name"])
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__category__is_active=True)

    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())
