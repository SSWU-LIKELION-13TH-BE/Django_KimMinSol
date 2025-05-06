from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from .forms import SignUpForm, LoginForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from board.models import Post

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
            return redirect('post_list')
    
    else :
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def home_view(request):
    return render(request, 'home.html')

CustomUser = get_user_model()

@login_required
def edit_profile(request) :
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid() :
            user = form.save(commit=False)
            if form.cleaned_data['password'] :
                user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('edit_profile')  

    else :
        form = UserUpdateForm(instance=request.user)
        
    return render(request, 'user/edit_profile.html', {'form': form})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'user/my_posts.html', {'posts': posts})