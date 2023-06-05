from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


def products_list(request):
    return render(request, 'storage/products_list.html')


class PruductView(DetailView):
    model = Product
    template_name = 'storage/product_room.html'
    context_object_name = 'product'
