from django.shortcuts import render
from django.http import HttpResponse
from Get_fuel_price import get_data, moded_Url, showing, table_Creation



def second_page(request):
    return HttpResponse('<h2> Something written here, should be smaller </h2>')

def scrapes(request):
    return render(request, 'idontknow/Fuel_home_page.html')

def table(request):
    prod_type = request.GET.get('product', '6')
    # table_Creation()
    return HttpResponse(get_data(prod_type))
