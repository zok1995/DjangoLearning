from django.shortcuts import render
from .forms import SubscriberForm
import time
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
