from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
                  path('', views.backend_home, name='backend-home'),
                  path('groups/', views.view_groups, name='view-groups'),
                  path('genres/', views.view_genres, name='view-genres'),
                  path('usergames/', views.view_user_games, name='view-usergames'),
                  path('users/', views.view_users, name='view-users'),
                  path('reviews/<int:review_id>/', views.ReviewDeleteView.as_view(), name='review-delete'),
                  path('games/', views.GameListView.as_view(), name='game-list'),
                  path('games/<int:game_id>/', views.GameDetailView.as_view(), name='game-detail'),
                  path('games/create/', views.GameCreateView.as_view(), name='game-create'),
                  path('reviews/', views.ReviewListView.as_view(), name='review-list'),
                  path('reviews/create/', views.ReviewCreateView.as_view(), name='review-create'),
                  path('api/genres/', views.GenreListView.as_view(), name='genre-list'),
                  path('api/user/', views.get_user_data, name='user-data'),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('register/', views.RegisterView.as_view(), name='register'),
                  path('reviews/<int:review_id>/update/', views.ReviewUpdateView.as_view(), name='review-update'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)