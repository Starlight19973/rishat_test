from django.shortcuts import render, get_object_or_404
from .models import Item
import stripe
from django.conf import settings
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


def item_view(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'item.html', context)


def create_checkout_session(request, id):
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/api/item/{id}'.format(id=id),
        cancel_url='http://127.0.0.1:8000/api/item/{id}'.format(id=id),
    )
    return JsonResponse({'id': session.id})
