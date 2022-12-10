from  django import forms
from .models import Raw

class RawForm(forms.ModelForm):
    class Meta:
        model = Raw
        fields = ['num', 'name', 'layer']
