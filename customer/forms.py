from .models import *
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.widgets  import PhoneNumberInternationalFallbackWidget,PhoneNumberPrefixWidget



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = {'createdat','modifiedat','owner__frist_name','modifiedby'}
        widgets = {
            'transaction_date': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': PhoneNumberPrefixWidget(attrs={'type': 'tel' , "class":"form-control"})
           
        }

