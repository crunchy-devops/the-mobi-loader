# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.http import FileResponse
from .models import MobiFile
from .forms import MobiFileForm
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
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')


def dashboard(request):
    if request.method == 'POST':
        form = MobiFileForm(request.POST, request.FILES)
        if form.is_valid():
            mobi_file = form.save(commit=False)
            mobi_file.uploaded_by = request.user
            mobi_file.name = request.FILES['file'].name
            mobi_file.save()
            return redirect('dashboard')
    else:
        form = MobiFileForm()

    files = MobiFile.objects.filter(uploaded_by=request.user).order_by('-uploaded_at')
    return render(request, 'dashboard.html', {'form': form, 'files': files})


def download_file(request, file_id):
    mobi_file = MobiFile.objects.get(pk=file_id)
    response = FileResponse(mobi_file.file)
    return response


def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def main_view(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect(settings.LOGIN_URL)

