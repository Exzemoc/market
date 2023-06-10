from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Product, Rating
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Avg


def products_list(request):
    return render(request, 'storage/products_list.html')


class PruductView(DetailView):
    model = Product
    template_name = 'storage/product_room.html'
    context_object_name = 'product'

@login_required
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    already_rated = Rating.objects.filter(product=product, user=request.user).exists()
    average_rating = Rating.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
    context = {
        'product': product,
        'already_rated': already_rated,
        'average_rating': average_rating,
    }
    return render(request, 'storage/product_room.html', context)

def rate_product(request, pk):
    if request.method == 'POST':
        rating_value = int(request.POST['rating'])
        product = get_object_or_404(Product, pk=pk)
        rating, created = Rating.objects.get_or_create(product=product, user=request.user)
        rating.rating = rating_value
        rating.save()
    return redirect('product_room', pk=pk)