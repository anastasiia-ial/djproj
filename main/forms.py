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
            'num': 'Артикул',
            'name': 'Наименование',
            'raw': 'Сырье ',
            'weight': 'Вес',
            'photo': 'Чертеж продукта',
        }

        widgets = {
            'num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите артикул'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите наименование'}),
            'raw': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вес'}),
        }
