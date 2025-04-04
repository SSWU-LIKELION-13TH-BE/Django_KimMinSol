from django.urls import path
from .views import post_create, post_list, toggle_like
from . import views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('like/<int:post_id>/', toggle_like, name='toggle_like'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
]
