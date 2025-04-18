from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm) :
    email = forms.EmailField(required=True)  # 이메일 필수

    class Meta :
        model = CustomUser
        fields = ['nickname', 'email', 'user_id', 'password1', 'password2']

class LoginForm(AuthenticationForm) :
    user_id = forms.CharField(
        label='아이디',
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력하세요'})
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력하세요'})
    )
    
    def __init__(self, request = None, *args, **kwargs) :
        super().__init__(request, *args, **kwargs)
        self.fields['username'] = self.fields.pop('user_id')

