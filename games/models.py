from django.db import models
from django.contrib.auth.models import AbstractUser

# In games/models.py
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=10, default='user')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.username


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=50, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['genre_name']),
        ]

    def __str__(self):
        return self.genre_name


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    release_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='games')
    maturity_rating = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title


class UserGame(models.Model):
    user_game_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='user_games')
    status = models.CharField(max_length=10, null=True, blank=True)  # e.g., 'completed', 'playing', 'backlog'
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'game']),
        ]
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"Review by {self.user.username} for {self.game.title}"