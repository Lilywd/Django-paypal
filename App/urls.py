from django.urls import path,include
from .views import *
from .import views

urlpatterns =[
    path('checkout', views.checkout, name='checkout'),
    path('paypal/', include("paypal.standard.ipn.urls")),
    path('payment-success/', payment_success_view, name="success"),
    path('payment-failed/', payment_failed_view, name="failed"),
  
] 