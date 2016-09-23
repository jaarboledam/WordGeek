from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'password': PasswordInput()
        }


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
