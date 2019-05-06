from django.db import models

class Payment(models.Model):
    orderNo = models.IntegerField()
    payAmount = models.IntegerField()
    paidAmount = models.IntegerField()
    paydate = models.DateTimeField()
    
    class Meta:
        db_table = 'payment'
