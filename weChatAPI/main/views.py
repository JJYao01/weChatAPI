from django.shortcuts import render
from payment.models import Payment


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    orders = Payment.objects.all()
    context = {'orders':orders}
    return render(request, 'main/main.html', context)