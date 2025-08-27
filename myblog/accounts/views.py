from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SigninForm, RegisterForm
from .models import CustomUser

# Create your views here.
def signin_view(request):
    if request.user.is_authenticated:
        return redirect('list')
    
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                next_URL = request.GET.get('next', 'list')
                return redirect(next_URL)
            else:
                messages.error(request, "Invalid email or password.")
    else:
       form =  SigninForm()

    return render(request, 'accounts/sign_in.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('list')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created successfully. Welcome, {user.username}!")
            return redirect('list')
        # The invalid form with errors will be passed to the template
    else:
        # This handles GET requests - show a blank form
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, f"You have logged out successfully.")
    return redirect('list')