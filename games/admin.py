from django.contrib import admin
from .models import User, Genre, Game, UserGame, Review

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role', 'created_at')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_id', 'genre_name')
    search_fields = ('genre_name',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'title', 'platform', 'release_date', 'publisher', 'genre')
    search_fields = ('title', 'publisher')
    list_filter = ('platform', 'genre', 'release_date')
    date_hierarchy = 'release_date'

@admin.register(UserGame)
class UserGameAdmin(admin.ModelAdmin):
    list_display = ('user_game_id', 'user', 'game', 'status', 'rating')
    search_fields = ('user__username', 'game__title')
    list_filter = ('status',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'user', 'game', 'rating', 'created_at')
    search_fields = ('user__username', 'game__title', 'review_text')
    list_filter = ('rating', 'created_at')
    date_hierarchy = 'created_at'