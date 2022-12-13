from django.shortcuts import render

from .models import Product, ProductCategory


def index(request):
    return render(request, 'products/index.html')


def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)
