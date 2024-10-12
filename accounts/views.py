from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('feed:feed_page')
    else:
        if request.method == 'POST':
            form = forms.CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('feed:feed_page')
        else:
            form = forms.CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')  
    else:
        form = forms.UserProfileForm(instance=user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('feed:feed_page')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('feed:feed_page')
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    
