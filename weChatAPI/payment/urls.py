from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from payment import views


router = DefaultRouter()
router.register(r'payment',views.PaymentViewSet)
    
app_name = 'payment'
urlpatterns = [
    path('', include(router.urls)),
]