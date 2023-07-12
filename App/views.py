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
        'invoice': 'Test Payment Invoice',
        'currency_code': 'USD',
        "notify_url":'http://{}{}'.format(host,reverse('paypal-ipn')),
        # "return": 'http://{}{}'.format(host,reverse('payment-success')),
        # "cancel_return": 'http://{}{}'.format(host,reverse('payment-failed')),
#       
        
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'App/index.html', {'form': form})

@csrf_exempt
def payment_success_view(request):
    context=request.POST
    return render(request, 'App/success.html')


@csrf_exempt
def payment_failed_view(request):
    context=request.POST
    return render(request, 'App/failed.html')