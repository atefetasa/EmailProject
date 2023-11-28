from django import forms
from .models import *


class CreateEmailModelForm(forms.ModelForm):
    class Meta:
        model = Email
        exclude = ['sender', 'draft', 'replied_email', 'deleted_by_user', 'read_by_user', 'archived_by_user']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'title',
                'id': 'title',
                'placeholder': 'enter email title'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '30',
                'rows': '4',
                'name': 'text',
                'id': 'text',
                'placeholder': 'enter email text'
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'name': 'file',
                'id': 'file',
                'placeholder': 'select the file'
            }),
        }

