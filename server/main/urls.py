from django.urls import path
from main.views import main_view, contact_view, products_view

urlpatterns = [
    path('', main_view),
    path('contact/', contact_view),
    path('products/', products_view),
]
