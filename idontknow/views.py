from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def second_page(request):
    return HttpResponse('<h2> Something written here, should be smaller </h2>')

def scrapes(request):
    return render(request, 'idontknow/Fuel_home_page.html')

# def scrapes(request):
#     return HttpResponse( 'Work_plz/TEST.html')
