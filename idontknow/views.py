from django.shortcuts import render
from Get_fuel_price import get_data, moded_Url, showing



def scrapes(request):
    return render(request, 'idontknow/Fuel_home_page.html')

def table(request):
    prod_type = int(request.GET.get('product', 6))
    random_list = {1:'91 Unleaded', 2:'95 Unleaded', 6:'98 Premium Unleaded', 4:'Disiel', 5:'LPG'}

    return render(request, 'Cheap_Fuel_Online/template_script.html', {'query': prod_type,
        'Fuel_types':random_list, 'something_regarding_fuel':get_data(ftype = prod_type)})
