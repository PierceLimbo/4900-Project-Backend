from django.urls import path
from . import views

urlpatterns = [
    path('', views.backend_home, name='backend-home'),
    path('groups/', views.view_groups, name='view-groups'),
    path('games/', views.view_games, name='view-games'),
    path('genres/', views.view_genres, name='view-genres'),
    path('reviews/', views.view_reviews, name='view-reviews'),
    path('usergames/', views.view_user_games, name='view-usergames'),
    path('users/', views.view_users, name='view-users'),
]
