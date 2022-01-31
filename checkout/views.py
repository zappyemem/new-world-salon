from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You do not have any product yet in your Cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KNuz9AP2LI77fqAphmvr8IynaRPmYL5lev2B4ZrdH15qusSEfN6Sv8HGS1qH1TDPLNQ84pO9V1MvHSlvkUrP8gc00YXs1B6dC',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
