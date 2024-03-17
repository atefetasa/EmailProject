from django import forms
from .models import *
from django.core import validators
from ckeditor.widgets import CKEditorWidget
from account_module.models import Signature


class CustomFileField(forms.FileField):
    pass


class CreateEmailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateEmailForm, self).__init__(*args, **kwargs)

        if self.request:
            self.fields['labels'].queryset = Label.objects.filter(creator=self.request.user)
            self.fields['signature'].queryset = Signature.objects.filter(user=self.request.user)

    class Meta:
        model = Email
        fields = ['title', 'text', 'attached_file', 'direct_receivers',
                  'cc_receivers', 'bcc_receivers', 'labels', 'signature', 'draft']
        labels = {
            'text': 'Email Text',
            'direct_receivers': 'to',
            'cc_receivers': 'cc',
            'bcc_receivers': 'bcc',
            'signature': 'Choose a signature to attach to the email',
            'labels': 'Choose a label'
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input1',
                'type': 'text',
                'placeholder': 'Enter email title',
                'name': 'email_title'
            }),
            'text': forms.Textarea(attrs={
                'class': 'email_body',
                'id': 'id_text',
                'type': 'text',
                'placeholder': 'Type email Text',
                'name': 'editor'
            }),
            'attached_file': forms.ClearableFileInput,
            'draft': forms.HiddenInput(attrs={
                'id': "draft"
            })

        }

    direct_receivers = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'hidden',
            'id': 'direct_receivers'
        })
    )

    cc_receivers = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'hidden',
            'id': 'cc_receivers'
        })
    )

    bcc_receivers = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'hidden',
            'id': 'bcc_receivers'
        })
    )

    labels = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    signature = forms.ModelChoiceField(
        queryset=None,
        required=False,
        widget=forms.RadioSelect,
        blank=True,
        empty_label='No signature'
    )

    def clean_attached_file(self):
        file = self.cleaned_data.get("attached_file")
        if file:
            if file.size > 25 * 1024 * 1024:
                raise forms.ValidationError("file size must be at most 25 Megabytes")

        return file
