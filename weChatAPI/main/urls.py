from django.urls import path, re_path, include
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('api/payment', include('payment.urls', namespace='payment')),    
    re_path('.*', views.main),
]