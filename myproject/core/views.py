from django.shortcuts import render
from django.http import JsonResponse
from .models import Product


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def products(request):
    products = Product.objects.values('title', 'price')
    data = [
        {
            'title': item['title'],
            'value': float(item['price'])
        }
        for item in products
    ]
    return JsonResponse(data, safe=False)
