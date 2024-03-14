from django import forms
from .models import *
from django.core import validators
from ckeditor.widgets import CKEditorWidget
from account_module.models import Signature


class CustomFileField(forms.FileField):
    pass


class CreateEmailForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CreateEmailForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['labels'].queryset = Label.objects.filter(creator=user)
            self.fields['signature'].queryset = Signature.objects.filter(user=user)

    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input1',
            'type': 'text',
            'placeholder': 'Enter email title',
            'name': 'email_title'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'email_body',
            'id': 'editor',
            'type': 'text',
            'placeholder': 'Type email Text',
            'name': 'editor'
        }),
        label='Email text'
    )

    attachment = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput,
    )

    to = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'hidden',
            'id': 'direct_receivers'
        })
    )

    cc = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'hidden',
            'id': 'cc_receivers'
        })
    )

    bcc = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'hidden',
            'id': 'bcc_receivers'
        })
    )

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Choose a label',
    )

    signature = forms.ModelChoiceField(
        queryset=Signature.objects.none(),
        required=False,
        widget=forms.RadioSelect,
        blank=True,
        label='Choose a signature to attach to the email',
        empty_label='No signature'
    )

    is_draft = forms.BooleanField(
        required=True,
        widget=forms.HiddenInput(attrs={
            'id': "draft"
        })
    )

    def clean_attachment(self):
        file = self.cleaned_data.get("attachment")
        if file:
            if file.size > 25 * 1024 * 1024:
                raise forms.ValidationError("file size must be at most 25 Megabytes")

        return file


