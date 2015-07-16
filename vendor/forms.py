from django import forms
from django.forms.formsets import formset_factory
from .models import *

class dishForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    calories = forms.FloatField()

class LogoForm(forms.Form):
    image = forms.ImageField()

class MenuForm(forms.Form):
    image = forms.ImageField()

class HourForm(forms.Form):
    opentime = forms.TimeField()
    closetime = forms.TimeField()
    d1 = forms.BooleanField()
    d2 = forms.BooleanField()
    d3 = forms.BooleanField()
    d4 = forms.BooleanField()
    d5 = forms.BooleanField()
    d6 = forms.BooleanField()
    d7 = forms.BooleanField()
    
