from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('name_user', 'surname_user', 'email_user', 'phone_user', 'adress_user', 'contact_user',)
