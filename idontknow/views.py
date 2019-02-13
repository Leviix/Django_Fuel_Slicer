from django.shortcuts import render
from django.http import HttpResponse
from Get_fuel_price import get_data as GFP


def second_page(request):
    return HttpResponse('<h2> Something written here, should be smaller </h2>')

def scrapes(request):
    return render(request, 'idontknow/Fuel_home_page.html')

def table(request):
    return HttpResponse(GFP())
