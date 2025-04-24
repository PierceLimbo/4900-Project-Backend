from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Game, Review, User
from .serializers import GameSerializer, ReviewSerializer, RegisterSerializer

class GameListView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "User created successfully."}, status=201)

    # User Data View (can be used to retrieve current user's data after login)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    user = request.user
    serializer = RegisterSerializer(user)
    return Response(serializer.data)

def backend_home(request):
    return render(request, 'backend_home.html')

from django.http import HttpResponse

def view_groups(request):
    return HttpResponse("Groups Data Page")

def view_games(request):
    return HttpResponse("Games Data Page")

def view_genres(request):
    return HttpResponse("Genres Data Page")

def view_reviews(request):
    return HttpResponse("Reviews Data Page")

def view_user_games(request):
    return HttpResponse("User Games Data Page")

def view_users(request):
    return HttpResponse("Users Data Page")