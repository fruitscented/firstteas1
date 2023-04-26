from .models import MenuItem
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'index.html', {})

def menu(request):
    menu_items = MenuItem.objects.all
    return render(request, 'menu.html', {'menu_items' : menu_items})

def menu_drinks(request):
    drink_list= MenuItem.objects.filter(menu_is_a_Drink=True)
    return render(request, 'menu_drinks.html', {'drink_list': drink_list})
def menu_snacks(request):
    snack_list= MenuItem.objects.filter(menu_is_a_Drink=False)
    return render(request, 'menu_snacks.html', {'snack_list': snack_list})

def cart(request):
    return render(request, 'cart.html', {})