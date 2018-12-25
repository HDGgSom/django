import json
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Good

def list_view(request):

    return render(
        request,
        'goods/list.html',
        {
            'goods': get_list_or_404(Good),
            'page_title': 'Перечень товаров'
        }

    )

def detail_view(request, pk):

    return render(
        request,
        'goods/detail.html',
        {
            'object': get_object_or_404(Good, id=pk)
        }
    )
