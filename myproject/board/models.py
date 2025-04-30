from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    tech_stack = models.CharField(max_length=100)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username}의 댓글" 

    def like_count(self):
        return self.likes.count()

    def is_liked_by(self, user):
        return self.likes.filter(user=user).exists()


    class Meta:
        ordering = ['created_at']

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('comment', 'user')

    def __str__(self):
        return f"{self.user.username} → {self.comment}"
