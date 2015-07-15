from django import forms


class LogoImageForm(forms.Form):
    image = forms.ImageField()
