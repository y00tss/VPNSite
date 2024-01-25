from django import forms
from django.contrib.auth.forms import UserCreationForm
from authorisation.models import CustomUser

# ------------------------------------------------Registration FORM------------------------------------------------


class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

# ------------------------------------------------Registration FORM------------------------------------------------


# ---------------------------------------------------EDITION FORM---------------------------------------------------


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'avatar')


# ---------------------------------------------------EDITION FORM---------------------------------------------------