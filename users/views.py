# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login # Import the login function
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a blank profile for the new user
            Profile.objects.create(user=user)
            # Log the user in automatically
            login(request, user)
            messages.success(request, f'Account created successfully! Please complete your profile.')
            # Redirect to the profile creation page
            return redirect('profile-update')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile') # After updating, go to the display page
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'users/profile_form.html', context)