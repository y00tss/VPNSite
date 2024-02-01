from django import forms
from django.contrib.auth.forms import UserCreationForm
from authorisation.models import CustomUser


class SignUpForm(UserCreationForm):
    """Registration form for new users"""

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password1',
            'password2',
        )


class ProfileEditForm(forms.ModelForm):
    """Edit form for user profile"""

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'avatar',
        )
