from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from .forms import SignUpForm, LoginForm, FindPasswordForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
        
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

CustomUser = get_user_model()

def find_password_view(request):
    password = None
    not_found = False

    if request.method == 'POST':
        form = FindPasswordForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            try:
                user = CustomUser.objects.get(user_id=user_id)
                password = user.password  # 실제론 해시된 값!
            except CustomUser.DoesNotExist:
                not_found = True
    else:
        form = FindPasswordForm()

    return render(request, 'find_password.html', {
        'form': form,
        'password': password,
        'not_found': not_found
    })