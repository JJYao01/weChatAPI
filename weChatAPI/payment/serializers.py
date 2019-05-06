from rest_framework import serializers
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        # fields = '__all__'
        fields = ('id', 'orderNo', 'payAmount', 'paidAmount', 'paydate')
