from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from workshop.accounts.models import PetstagramUser

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password'
            }
        )
    )


class EditUserForm(forms.ModelForm):
    class Meta:
        model = PetstagramUser
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender']
        exclude = ['password']
        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'profile_picture': 'Image',
            'gender': 'Gender'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['profile_picture'].widget.attrs['placeholder'] = 'Link to profile picture'


