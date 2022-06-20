from django.shortcuts import render
from .models import Order

# Create your views here.
def index(request):
    orders = Order.objects.all()
    order_numbers = orders.count()
    context = {
        'orders': orders,
        'order_numbers': order_numbers
    }
    return render(request, 'index.html', context)