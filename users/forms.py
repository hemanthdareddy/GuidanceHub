from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile # Import the Profile model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Add this new form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # List all the fields from the Profile model you want the user to edit
        fields = [
            'full_name', 'profile_picture', 'phone_number', 'date_of_birth', 
            'gender', 'country', 'college', 'branch', 
            'graduation_year', 'academic_status'
        ]