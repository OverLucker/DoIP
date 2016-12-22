from django import forms
import django.forms.widgets as widgets
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


def validate_password(password):
    if len(password) < 8:
        raise forms.ValidationError(
            _("Password length should be at least 8 characters"),
            code='invalid'
        )


def validate_username(username):
    if len(username) < 5:
        raise forms.ValidationError(
            _("Username length should be at least 5 characters"),
            code='invalid'
        )
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError(
            _("This username is already taken"),
            code="invalid"
        )


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=widgets.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control input-sm',
            }
        ),
        max_length=150,
        validators=[validate_username]
    )
    password1 = forms.CharField(
        label='Password',
        widget=widgets.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control input-sm',
            }
        ),
        max_length=100,
        validators=[validate_password]
    )
    password2 = forms.CharField(
        label='Password confirm',
        widget=widgets.PasswordInput(
            attrs={
                'placeholder': 'Password confirmation',
                'class': 'form-control input-sm',
            }
        ),
        max_length=100
    )
    email = forms.EmailField(
        label='E-mail',
        widget=widgets.EmailInput(
            attrs={
                'placeholder': 'E-mail',
                'class': 'form-control input-sm',
            }
        ),
        max_length=500
    )
    family_name = forms.CharField(
        label='Family name',
        widget=widgets.TextInput(
            attrs={
                'placeholder': 'Family name',
                'class': 'form-control input-sm',
            }
        ),
        max_length=30
    )
    first_name = forms.CharField(
        label='First name',
        widget=widgets.TextInput(
            attrs={
                'placeholder': 'First name',
                'class': 'form-control input-sm',
            }
        ),
        max_length=30
    )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError(
                _("Passwords should match"),
                code='invalid'
            )

        return cleaned_data

    def save(self):
        return User.objects.create(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['family_name']
        )


class AuthorizationForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=widgets.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control input-sm',
            }
        ),
        max_length=100
    )
    password = forms.CharField(
        label='Password',
        widget=widgets.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control input-sm',
            }
        ),
        max_length=100
    )
