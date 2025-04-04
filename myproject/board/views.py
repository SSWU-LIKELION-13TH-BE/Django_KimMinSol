from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

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

@login_required(login_url='/user/login/?next=/board/')
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_list'))
