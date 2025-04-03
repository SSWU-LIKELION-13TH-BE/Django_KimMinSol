from django.urls import path
from .views import signup_view, login_view, logout_view, find_password_view, home_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('find_password/', find_password_view, name = 'find_password'),
    path('', home_view, name='home'),
]
