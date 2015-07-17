from django import forms
from django.db import models
from django.forms import ModelForm
from django.forms.formsets import formset_factory
from .models import *

class dishForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    calories = forms.FloatField()
    isdelete = forms.BooleanField(initial=False, required=False)


class LogoForm(forms.Form):
    image = forms.ImageField()


class MenuForm(forms.Form):
    image = forms.ImageField()


class HourForm(ModelForm):
    class Meta:
        model = Hours
        fields = ['open_time', 'close_time', 'm', 't', 'w', 'r','f','s','h']
        #    opentime = forms.TimeField()
        #    closetime = forms.TimeField()
        #    d1 = forms.BooleanField()
        #    d2 = forms.BooleanField()
        #    d3 = forms.BooleanField()
        #    d4 = forms.BooleanField()
        #    d5 = forms.BooleanField()
        #    d6 = forms.BooleanField()
        #    d7 = forms.BooleanField()
    
