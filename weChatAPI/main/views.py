from django.shortcuts import render
from payment.models import Payment


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    orders = Payment.objects.all().exclude(customerName=None).order_by('-id')
    context = {'orders':orders}
    return render(request, 'main/main.html', context)