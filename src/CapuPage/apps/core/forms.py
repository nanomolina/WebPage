 # -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    """
    Forma para el ingreso del usuario al sistema
    """
    username = forms.RegexField(
        max_length = 30,
        regex=r"^[\w.@+-]+$",
        widget = forms.TextInput(
            attrs = {
                'class': "form-control",
                'id': 'user',
                'required': 'true',
            }
        )
    )
    password = forms.CharField(
        max_length = 30,
        widget = forms.PasswordInput(
                attrs = {
                    'class': "form-control",
                    'id': 'password',
                    'required': 'true',
                }
            )
        )

    class Meta:
        model = User
        fields = ('username', 'password')
