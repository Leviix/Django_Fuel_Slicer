from django.urls import path, re_path, include
# from Cheap_Fuel_Online import views
from . import views

urlpatterns = [
    path('/scrape', views.scrapes, name = 'scrapping'),
    path('table/', views.table, name = 'slice'),
]
