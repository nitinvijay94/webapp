from django import forms


class LogoImageForm(forms.Form):
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
