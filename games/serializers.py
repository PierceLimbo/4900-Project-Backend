from rest_framework import serializers
from .models import Game, Review
from django.db.models import Avg
from django.contrib.auth.password_validation import validate_password
from .models import User

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
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User  # Using the custom User model
        fields = ['username', 'password', 'password2', 'email', 'role']
        extra_kwargs = {
            'email': {'required': True},
            'role': {'required': False, 'default': 'user'},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', 'user')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user