from django.urls import path
from .views import post_create, post_list, toggle_like

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('like/<int:post_id>/', toggle_like, name='toggle_like'),
]
