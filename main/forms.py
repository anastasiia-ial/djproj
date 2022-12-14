from  django import forms
from .models import Raw, Sku

class RawForm(forms.ModelForm):
    class Meta:
        model = Raw
        fields = ['num', 'name', 'layer']

class SkuForm(forms.ModelForm):
    class Meta:
        model = Sku
        fields = ['num', 'name', 'raw','weight','photo']
