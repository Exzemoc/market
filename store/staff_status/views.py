from django.core.files.storage import default_storage
from django.shortcuts import render
from users.models import Order
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from storage.models import Product, ProductImage



@login_required
def staff_page(request):
    # Получение всех заказов
    user = request.user
    if user.is_staff:
        orders = Order.objects.all()
        context = {
            'orders': orders
        }
        return render(request, 'staff_status/staff_page.html', context)
    else:
        return HttpResponse('У вас нет доступа к этой странице.')


def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_confirmed = True
    order.save()
    return redirect('staff_orders')


def close_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('staff_orders')


def create_product(request):

    user = request.user
    if user.is_staff:

        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            tip = request.POST.get('tip')
            description = request.POST.get('description')
            date_release = request.POST.get('date_release')
            image = request.FILES.get('image')  # Получение загруженного изображения

            product = Product.objects.create(
                name=name,
                price=price,
                tip=tip,
                description=description,
                date_release=date_release
            )
            if image:
                # Генерация уникального имени файла
                image_name = default_storage.get_available_name(image.name)
                # Сохранение изображения в медиафайлы
                image_path = default_storage.save(f'media/{image_name}', image)
                # Создание объекта ProductImage
                product_image = ProductImage.objects.create(
                    product=product,
                    image=image_path
                )
            return redirect('products_list')  # Перенаправление на страницу со списком продуктов
    else:
        return HttpResponse('У вас нет доступа к этой странице.')

    return render(request, 'staff_status/add_product.html')
