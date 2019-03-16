from django.shortcuts import render
from Get_fuel_price import get_data, moded_Url, showing, table_Creation



def scrapes(request):
    return render(request, 'idontknow/Fuel_home_page.html')

def table(request):
    prod_type = int(request.GET.get('product', 6))
    random_list = {1:'91 Unleaded', 2:'95 Unleaded', 6:'98 Premium Unleaded', 4:'Disiel', 5:'LPG'}
    EI = random_list.items()
    return render(request, 'Cheap_Fuel_Online/template_script.html', {'query': prod_type,
        'list':random_list, 'something_regarding_fuel':get_data(ftype = prod_type)})
