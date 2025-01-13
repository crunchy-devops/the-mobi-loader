# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings

#from django.contrib.auth.models import User

# Create a user with a username, email, and password
#user = User.objects.create_user('username', 'email@example.com', 'password123')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def main_view(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        return redirect(settings.LOGIN_URL)

