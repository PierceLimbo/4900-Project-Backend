from rest_framework import serializers
from django.db.models import Avg
from .models import Game, Review, Genre, User


class GameSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField(read_only=True)
    genre_name = serializers.CharField(source='genre.genre_name', read_only=True)

    class Meta:
        model = Game
        fields = ['game_id', 'title', 'platform', 'release_date', 'publisher',
                  'description', 'genre', 'genre_name', 'maturity_rating', 'image', 'average_rating']
        read_only_fields = ['game_id']

    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg is not None else 0


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    game_title = serializers.CharField(source='game.title', read_only=True)

    class Meta:
        model = Review
        fields = ['review_id', 'user', 'username', 'game', 'game_title', 'rating', 'review_text', 'created_at']
        read_only_fields = ['review_id', 'user', 'username', 'game_title', 'created_at']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_id', 'genre_name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'role']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', 'user')
        )
        user.set_password(validated_data['password'])
        user.save()

        return user