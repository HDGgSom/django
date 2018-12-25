from django.urls import path
from main.views import main_view, contact_view, products_view

app_name = "main"

urlpatterns = [
    path('', main_view, name='main'),
    path('contacts/', contact_view, name='contact'),
    path('my_products/', products_view, name='products'),
]
