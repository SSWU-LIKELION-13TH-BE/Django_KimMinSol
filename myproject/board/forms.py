from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'tech_stack', 'github_url']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '댓글을 작성하세요'}),
        }

        def __init__(self, *args, **kwargs):
            post = kwargs.get('post', None)
            super().__init__(*args, **kwargs)
            
            if post:
                self.fields['parent'].queryset = post.comments.filter(parent=None) 