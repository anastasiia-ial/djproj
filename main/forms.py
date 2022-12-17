from django import forms
from django.forms import ModelForm
from .models import *


class RawForm(forms.ModelForm):
    class Meta:
        model = Raw
        fields = ['num', 'name', 'layer']


class SkuForm(forms.ModelForm):
    class Meta:
        model = Sku
        fields = ('num', 'name', 'raw', 'weight', 'photo')
        labels = {
            'num': '',
            'name': '',
            'raw': 'Сырье ',
            'weight': '',
            'photo': '',
        }

        widgets = {
            'num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Артикул'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование'}),
            'raw': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Вес'}),
        }
