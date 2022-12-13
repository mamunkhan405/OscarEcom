from oscar.apps.payment.models import *  # noqa isort:skip
from django.db import models
import uuid
from apps.order.models import *

class Payment(models.Model):
    purchid = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase')
    amount = models.FloatField(default=0)

    def __str__(self):
        return str(self.purchid)
    
#