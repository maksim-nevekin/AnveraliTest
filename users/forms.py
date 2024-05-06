from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "role",
            "first_name",
            "last_name",
            "username",
            "email",
            "experience",
            "password1",
            "password2",
        )

    role = forms.ChoiceField(choices=(('customer', 'Заказчик'), ('executor', 'Исполнитель')))
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    experience = forms.IntegerField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
            "experience",
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    experience = forms.IntegerField()
