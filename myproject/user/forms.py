from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Guestbook
from django.contrib.auth import get_user_model

User = get_user_model()

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

class UserUpdateForm(forms.ModelForm) :
    password = forms.CharField(widget = forms.PasswordInput(), required = False)

    class Meta :
        model = User
        fields = ['user_id', 'nickname', 'email', 'password']

class GuestbookForm(forms.ModelForm) :

    class Meta:
        model = Guestbook
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs = {'placeholder': '방명록을 작성해주세요!', 'rows': 3}),
        }

