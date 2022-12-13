from django.forms import ModelForm
from django import forms
from .models import *
from apps.order.models import *
from apps.payment.models import *

from django.contrib.admin import widgets


class CreateUserForm(ModelForm):
    firstname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
   
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['firstname'].widget.attrs['class'] = 'form-control'
        self.fields['lastname'].widget.attrs['class'] = 'form-control'
        self.fields['img'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'

class CreatePurchaseForm(ModelForm):
       
    class Meta:
        model = Purchase
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreatePurchaseForm, self).__init__(*args, **kwargs)

        self.fields['uid'].widget.attrs['class'] = 'form-control'
        self.fields['purchid'].widget.attrs['class'] = 'form-control'
        self.fields['productid'].widget.attrs['class'] = 'form-control'

class CreatePaymentForm(ModelForm):
   
    class Meta:
        model = Payment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreatePaymentForm, self).__init__(*args, **kwargs)

        self.fields['purchid'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'


