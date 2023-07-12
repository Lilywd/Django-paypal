import uuid
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

def checkout(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '100',	
        'item_name': 'Item_Name_xyz',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url':f'http://{host}{reverse("paypal-ipn")}',
        'return': f'http://{host}{reverse("payment-success")}',
        'cancel_return': f'http://{host}{reverse("payment-failed")}',
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'App/checkout.html', {'form': form})


def payment_success(request):
    return redirect('success')


def payment_failed(request):
      return redirect('failed')