from django.db import models

class Payment(models.Model):
    orderNo = models.IntegerField()
    customerName = models.TextField(default=None, blank=True, null=True)
    itemName = models.TextField(default=None, blank=True, null=True)
    payAmount = models.IntegerField()
    paydate = models.DateTimeField()    
    
    class Meta:
        db_table = 'payment'
