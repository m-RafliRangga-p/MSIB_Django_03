from django import forms
from .models import Customer

class NewSubscriber(forms.ModelForm):
    class Meta():
        model = Customer
        fields = '__all__'