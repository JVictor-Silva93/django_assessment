from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index page with assessment instructions
    path('posts/', views.post_list, name='post_list'),  # List all blog posts
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # Detail view for a single post
]
