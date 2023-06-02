import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.django_forms import add_placeholder, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu usuário')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: João')
        add_placeholder(self.fields['last_name'], 'Ex.: Oliveira')
        add_placeholder(self.fields['password'], 'Digite sua senha')
        add_placeholder(self.fields['password2'], 'Digite a senha novamente')

    username = forms.CharField(
        label='Usuario',
        help_text=(
            'O usuário deve ter letras, numeros ou um desses caracteres @.+-_'
            'O tamanho deve estar entre 4 e 20 caracteres.'
        ),
        error_messages={
            'required': 'Este campo não pode ser vazio.',
            'min_length': 'Usuário deve ter pelo menos 4 caracteres',
            'max_length': 'Usuario deve ter menos de 20 caracteres',
        },
        min_length=4, max_length=20,
    )
    first_name = forms.CharField(
        error_messages={'required': 'Escreva seu primeiro nome'},
        label='Nome'
    )
    last_name = forms.CharField(
        error_messages={'required': 'Escreva seu sobrenome'},
        label='Sobrenome'
    )
    email = forms.EmailField(
        error_messages={'required': 'E-mail é obrigatório'},
        label='E-mail',
        help_text='O e-mail deve ser válido.',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'A senha não pode ser vazia'
        },
        help_text=(
            'Senha deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O tamanho deve ser de '
            'pelo menos 8 caracteres.'
        ),
        validators=[strong_password],
        label='Senha'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha',
        error_messages={
            'required': 'Por favor, repita sua senha'
        },
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'E-mail já está em uso', code='invalid',
            )

        return email


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })