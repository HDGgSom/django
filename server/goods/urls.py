from django.urls import path
from goods.views import list_view, detail_view

app_name = "goods"

urlpatterns = [
    path('', list_view, name='index'),
    path('<int:pk>/', detail_view, name='detail'),
]

