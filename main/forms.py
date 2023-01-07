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
        fields = ('type','num', 'name', 'raw', 'weight', 'photo')
        labels = {
            'type': 'Тип продукции',
            'num': 'Артикул',
            'name': 'Наименование',
            'raw': 'Сырье ',
            'weight': 'Вес',
            'photo': 'Чертеж продукта',
        }

        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите артикул'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите наименование'}),
            'raw': forms.SelectMultiple(attrs={'class': 'form-control', }),
            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вес'}),
        }

class ChangeForm(forms.ModelForm):
    class Meta:
        model = Change
        fields = ('raw_current', 'raw_new', 'created_date')
        labels = {
            'raw_current': 'Текущее сырье',
            'raw_new': 'Новое сырье ',
           
        }

        widgets = {
            'raw_current': forms.Select (attrs={'class': 'form-control'}),
            'raw_new': forms.Select (attrs={'class': 'form-control'}),
           
        }