from . import views
from django.urls import path
from .views import GameListView, ReviewListView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('', views.backend_home, name='backend-home'),
    path('groups/', views.view_groups, name='view-groups'),

    # path('games/', views.view_games, name='view-games'),

    path('genres/', views.view_genres, name='view-genres'),
    # path('reviews/', views.view_reviews, name='view-reviews'),
    path('usergames/', views.view_user_games, name='view-usergames'),
    path('users/', views.view_users, name='view-users'),

    # working JSON API
    path('games/', GameListView.as_view(), name='api-games'),
    path('reviews/', ReviewListView.as_view(), name='api-reviews'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

