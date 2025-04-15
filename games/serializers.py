from rest_framework import serializers
from .models import Game, Review

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    game = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['review_id', 'user', 'game', 'rating', 'review_text', 'created_at']
