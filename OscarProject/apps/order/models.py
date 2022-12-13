from oscar.apps.order.models import *  # noqa isort:skip
from django.db import models
import uuid
from apps.customer.models import *

class Purchase(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    purchid = models.CharField(max_length=50)#auto generate during order process
    productid = models.ForeignKey('catalogue.Product', on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return str(self.purchid)
    
    