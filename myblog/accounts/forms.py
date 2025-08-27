from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'profile_pic', 'date_of_birth')

class SigninForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username.'
        })
    )
    password = forms.CharField(
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password.'
        })
    )

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email.'
        })
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your First Name'
        })
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Last Name'
        })
    )

    class Meta:
        model = CustomUser  # Or use get_user_model() if you're using custom user model
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        
        # Update widget attributes for the inherited fields
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter your username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose your password'
        })
        
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
            
            
            