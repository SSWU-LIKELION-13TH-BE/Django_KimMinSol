from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, CommentLike
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

@login_required(login_url='/user/login/') 
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('post_list') 

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

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(parent = None)
    
    if request.method == 'POST':
        parent_id = request.POST.get('parent')
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.post = post  
            comment.author = request.user  
            comment.save()

            if parent_id:
                try:
                    parent_comment = Comment.objects.get(id=parent_id)
                    comment.parent = parent_comment
                except Comment.DoesNotExist:
                    pass 

            comment.save()
            return redirect('post_detail', post_id = post.id)  

    else:
        comment_form = CommentForm()

    return render(request, 'board/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required(login_url='/user/login/')
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:  
        return redirect('post_detail', post_id=post.id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)  
    else:
        form = PostForm(instance=post)

    return render(request, 'board/post_edit.html', {'form': form})

@login_required(login_url='/user/login/')
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:  
        return redirect('post_detail', post_id=post.id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  
    
    return render(request, 'board/post_delete.html', {'post': post})

@login_required(login_url='/user/login/')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id  

    if request.user == comment.author:
        comment.delete()
    return redirect('post_detail', post_id=post_id)

@require_POST
@login_required(login_url='/user/login/')
def toggle_comment_like(request):
    comment_id = request.POST.get('comment_id')
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user

    like, created = CommentLike.objects.get_or_create(comment=comment, user=user)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': comment.like_count()
    })