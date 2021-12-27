from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from . import models

import sys
sys.path.append('..')
from management.models import User

MERCHANT = ''
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = ''  # Optional
mobile = ''  # Optional
CallbackURL = 'http://localhost:8000/zarinpal/verify/' # Important: need to edit for realy server.


def send_request(request):

    phonenumber = request.GET.get('phonenumber', '')
    amount = request.GET.get('amount', '')

    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)

    user = User.objects.get(phone_number=phonenumber)
    payment = models.Payments()
    payment.user = user
    payment.amount = int(amount)
    payment.token = result['Authority']
    payment.save()

    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            payment = models.Payments.objects.get(token=request.GET['Authority'])
            payment.user.money = payment.user.money + payment.amount
            payment.is_paid = True
            payment.save()
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')

