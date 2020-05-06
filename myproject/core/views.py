from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def products(request):
    products = Product.objects.values('title', 'price')
    data = {
        'data': [
            {
                'title': item['title'],
                'value': float(item['price'])
            }
            for item in products
        ]
    }
    return JsonResponse(data)


def categories(request):
    categories = Product.objects\
        .values('category')\
        .annotate(value=Count('category'))\
        .order_by('category')\
        .values('category__title', 'value')
    data = {
        'data': [
            {
                'label': item['category__title'],
                'value': item['value'],
            }
            for item in categories
        ]
    }
    return JsonResponse(data)
