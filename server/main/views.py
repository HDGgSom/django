from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template

def main_view(request):

    return render(
        request, 
        'main/index.html',
        {
            'page_title': 'Магазин',
        }
    )

def contact_view(request):

    return render(
        request, 
        'main/contact.html',
        {
            'page_title': 'Контакты',
        }
    )

def products_view(request):
    return render(
        request,
        'main/products.html',
        {
            'page_title': 'Каталог',
        }
    )