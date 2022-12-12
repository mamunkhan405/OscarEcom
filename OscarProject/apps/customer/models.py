from oscar.apps.customer.models import *  # noqa isort:skip
from django.db import models
import uuid

class User(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    firstname = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150, blank=True, null=True)
    img = models.ImageField(upload_to='User', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return str(self.uid)+self.firstname