from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort_value = request.GET.get('sort')
    sort_types ={'name':'name', 'min_price':'price', 'max_price':'-price', '':'id'}
    if sort_value:
        phones = Phone.objects.order_by(sort_types[request.GET['sort']])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

