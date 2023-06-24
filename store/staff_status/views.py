from django.shortcuts import render
from users.models import Order
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http import HttpResponse


@login_required
def staff_page(request):
    # Получение всех заказов
    user = request.user
    if user.groups.filter(name='Статус персонала').exists():
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