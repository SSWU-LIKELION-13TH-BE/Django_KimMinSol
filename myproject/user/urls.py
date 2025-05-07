from django.urls import path
from .views import signup_view, login_view, logout_view, home_view
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('mypage/edit/', views.edit_profile, name='edit_profile'),
    path('mypage/posts/', views.my_posts, name='my_posts'),
    path('user/<str:user_id>/guestbook/', views.guestbook_view, name='guestbook'),
    path('user/<str:user_id>/profile/', views.user_profile, name='user_profile'),

]
