from dataclasses import fields
from pydoc import describe
from pyexpat import model
from wsgiref import validate
from rest_framework import serializers
from apps.customer.models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    