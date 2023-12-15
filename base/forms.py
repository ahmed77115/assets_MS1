from django.forms import ModelForm
from .models import Office,User
from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.widgets  import PhoneNumberInternationalFallbackWidget,PhoneNumberPrefixWidget

# from .models import *
import datetime
# from dal import autocomplete
# from django.contrib.auth.models import User, Group, Permission, ContentType
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        # exclude = {'createdat','modifiedat','owner','modifiedby'}
        # widgets = {
        #     'transaction_date': forms.DateInput(attrs={'type': 'date'}),
        #     'phone_number': PhoneNumberInternationalFallbackWidget(),
           
        # }




class OfficeForm(ModelForm):
    class Meta:
        model = Office
        exclude = {'createdat','modifiedat','owner','modifiedby'}
  
# class DelvryForm(ModelForm):
#     class Meta:
#         model = Delvry
#         exclude = {'createdat','modifiedat','owner','modifiedby'}
  
# class ParcelForm(ModelForm):
#     class Meta:
#         model = Parcel
#         exclude = {'createdat','modifiedat','owner','modifiedby'}
#         widgets = {
#             'Date': forms.TimeInput(attrs={'type': 'date'}),
#             'delivery_time': forms.TimeInput(attrs={'type': 'date'}),
#             'time_receipt': forms.TimeInput(attrs={'type': 'date'}),
           
#         }
        



