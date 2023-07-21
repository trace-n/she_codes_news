#users/forms.py

from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #PasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

# class CustomUserChangeForm(UserChangeForm):
class CustomUserChangeForm(forms.ModelForm):

    # password = ReadOnlyPasswordHashField(
    #     label = ("Password"),
    #     help_text = (
    #         "Raw passwords are not stored, so there is no way to see this "
    #         "user’s password, but you can change the password using "
    #         '<a href="{users:change-password}">this form</a>.'
    #     ),
    # )

    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name', 'last_name'] 


# class CustomUserChangePasswordForm(PasswordChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ['password'] 