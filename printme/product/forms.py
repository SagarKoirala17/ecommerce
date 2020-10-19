from django import forms
from .models import Product
from design.models import Design


class DesignForm(forms.ModelForm):

    class Meta:
        model = Design
        fields = '__all__'

