import json
from operator import mod
from statistics import mode
import django

from django.forms import FloatField


def user_api_dict(users):
    user_dict = {
        'users':users,
        
    }
    return json.dumps(user_dict)