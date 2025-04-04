from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required(login_url='/user/login/') 
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('/') 

    else:
        form = PostForm()
    return render(request, 'board/post_create.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at') 
    return render(request, 'board/post_list.html', {'posts': posts})
