from rest_framework import serializers
from .models import Game, Review
from django.db.models import Avg

class GameSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    genre = serializers.StringRelatedField()

    class Meta:
        model = Game
        fields = '__all__'  # or list fields explicitly and include 'average_rating'

    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg is not None else 0


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    game = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['review_id', 'user', 'game', 'rating', 'review_text', 'created_at']
