from django import forms
from .models import *


class CreateEmailModelForm(forms.ModelForm):
    class Meta:
        model = Email

