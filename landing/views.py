from django.shortcuts import render
import time
# Create your views here.

def landing(request):
    name = "Oleksandr"
    currentDay = time.strftime("%H:%M:%S")
    return render(request, 'landing/landing.html', locals())
