from django.shortcuts import render
from django.http import HttpResponse
from Get_fuel_price import get_data, moded_Url, showing, table_Creation



def second_page(request):
    return HttpResponse('<h2> Something written here, should be smaller </h2>')

def scrapes(request):
    return render(request, 'idontknow/Fuel_home_page.html')




def table(request):
    prod_type = int(request.GET.get('product', '6'))

    fuel_type = [{1:'91 Unleaded',2:'95 Unleaded',6:'98 Premium Unleaded',4:'Disiel',5:'LPG'}]

    print(type(prod_type), type(fuel_type))
    options = ''.join('<option value="{V}" {chosen}>{product}</option>'.format(
        V = prod_type, chosen = 'selected' if V == prod_type else '', product = fuel_type)
        for prod_type in fuel_type[prod_type])

    return render(request, 'Cheap_Fuel_Online/template_script.html',{'options':options,
        'something_regarding_fuel':get_data(ftype = prod_type)})
