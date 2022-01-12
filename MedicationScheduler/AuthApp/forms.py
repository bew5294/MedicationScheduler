from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                   label="Current password")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                    label="New password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                    label="Repeat new password")

    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name']

    email = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Email")
    username = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Username")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="First Name")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Last Name")

