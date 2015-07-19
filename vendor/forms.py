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


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['address', 'latitude', 'longitude']


class HourForm(ModelForm):
    class Meta:
        model = Hours
        fields = ['open_time_m', 'close_time_m','open_time_t', 'close_time_t', 'open_time_w', 'close_time_w', 'open_time_r', 'close_time_r', 'open_time_f', 'close_time_f', 'open_time_s', 'close_time_s', 'open_time_h', 'close_time_h', 'm', 't', 'w',
                  'r', 'f', 's', 'h', 'leftTime']
