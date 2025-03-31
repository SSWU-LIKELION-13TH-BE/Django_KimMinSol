from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('signup')
        
    else :
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    
    else :
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def home_view(request):
    return render(request, 'home.html')