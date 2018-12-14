from django.shortcuts import render

def main_view(request):
    return render(request, 'main/index.html')

def contact_view(request):
    return render(request, 'main/contact.html')

def products_view(request):
    return render(request, 'main/products.html')