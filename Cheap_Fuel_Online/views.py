from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'Cheap_Fuel_Online/Home_page.html')

def about_us(request):
    return render(request, 'Cheap_Fuel_Online/about_us.html')
