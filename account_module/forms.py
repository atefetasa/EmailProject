from django import forms
import re
from .models import User
from django.core import validators


class RegisterModelForm(forms.ModelForm):
    password2 = forms.CharField(max_length=12,
                                required=True,
                                label='Confirm password',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'input100',
                                    'type': 'password',
                                    'name': 'conf_pass',
                                    'placeholder': 're enter your password'
                                }))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')
        if not email and not phone_number:
            raise forms.ValidationError("you must provide either an email address or phone number")

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            numbers = re.findall("\d", username)
            if (len(username) > 30) or (len(username) < 5):
                raise forms.ValidationError("username length should be between 5 and 30 characters")

            if len(numbers) > 4:
                raise forms.ValidationError("your username shouldn't contain more than 4 numerical characters")

        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
                raise forms.ValidationError(
                    "The password must contain at least 1 symbol: " + "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
                )

            if not re.findall('[a-z]', password):
                raise forms.ValidationError("The password must contain at least 1 lowercase letter, a-z.")

            if not re.findall('[A-Z]', password):
                raise forms.ValidationError("The password must contain at least 1 uppercase letter, A-Z.")

            if not re.findall('\d', password):
                raise forms.ValidationError("The password must contain at least 1 digit, 0-9.")

            if len(password) < 8 or len(password) > 12:
                raise forms.ValidationError(
                    "your chosen password must be between 8 and 12 characters"
                )

        return password

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            phone_pattern = r"^09"
            if len(phone_number) != 11:
                raise forms.ValidationError("phone number should be 11 digits")

            if (not re.search(phone_pattern, phone_number)) or (re.findall("\s", phone_number)):
                raise forms.ValidationError("phone number format is not correct")
        return phone_number

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("password and password confirmation must match")

        return password2

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'phone_number']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input100',
                'type': 'text',
                'name': 'username',
                'placeholder': 'Enter your username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'input100',
                'type': 'password',
                'name': 'pass',
                'placeholder': 'Enter your password'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input100',
                'type': 'email',
                'name': 'reco_email',
                'placeholder': 'Enter your recovery email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input100',
                'type': 'tel',
                'name': 'phone_number',
                'placeholder': 'Enter your phone number'
            }),
        }


class EnterCodeForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Enter the received Code',
            'class': 'input100',
            'name': 'active_code'
        }),
        validators=[
            validators.MaxLengthValidator(6)
        ]
    )

    def clean_code(self):
        entered_code = self.cleaned_data.get('code')
        if not entered_code.isdigit():
            raise forms.ValidationError("Only numerical characters are allowed.")

        return entered_code


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='username',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your username',
            'class': 'input100',
            'name': 'username'
        })
    )
    password = forms.CharField(
        max_length=12,
        required=True,
        label='password',
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'placeholder': 'Type your password',
            'class': 'input100',
            'name': 'pass'
        })
    )


class EnterEmailForm(forms.Form):
    recovery_email = forms.CharField(
        required=True,
        label='email address',
        widget=forms.EmailInput(attrs={
            'class': 'input100',
            'type': 'email',
            'name': 'reco_email',
            'placeholder': 'Enter your recovery email'
        }),
        validators=[
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        max_length=12,
        required=True,
        label='password',
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'placeholder': 'Enter your new password',
            'class': 'input100',
            'name': 'pass'
        })
    )

    confirm_password = forms.CharField(
        max_length=12,
        required=True,
        label='confirm password',
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
            'type': 'password',
            'name': 'password_conf',
            'placeholder': 're enter your password'
        })
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
                raise forms.ValidationError(
                    "The password must contain at least 1 symbol: " + "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
                )

            if not re.findall('[a-z]', password):
                raise forms.ValidationError("The password must contain at least 1 lowercase letter, a-z.")

            if not re.findall('[A-Z]', password):
                raise forms.ValidationError("The password must contain at least 1 uppercase letter, A-Z.")

            if not re.findall('\d', password):
                raise forms.ValidationError("The password must contain at least 1 digit, 0-9.")

            if len(password) < 8 or len(password) > 12:
                raise forms.ValidationError(
                    "your chosen password must be between 8 and 12 characters"
                )

        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("password and password confirmation must match")

        return confirm_password


