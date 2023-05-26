# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    phone_number = forms.CharField(max_length=20, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'phone_number',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Add your email validation logic here
        # For example, check if the email is already registered
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        # Remove any non-digit characters from the phone number
        phone_number = ''.join(filter(str.isdigit, phone_number))

        if len(phone_number) != 10:
            raise forms.ValidationError('Invalid phone number. Please enter a 10-digit number.')

        return phone_number



from django import forms
from .models import Vlog

class VlogForm(forms.ModelForm):
    class Meta:
        model = Vlog
        fields = ['image', 'title', 'details', 'date']

from django import forms
from .models import Comment

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'message')
