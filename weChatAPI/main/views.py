from django.shortcuts import render


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    context = {'like':'很棒'}
    return render(request, 'main/main.html', context)