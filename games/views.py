from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Game, Review, User, Genre
from .serializers import GameSerializer, ReviewSerializer, RegisterSerializer, GenreSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework.exceptions import PermissionDenied


class ReviewUpdateView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'review_id'
    lookup_url_kwarg = 'review_id'

    def perform_update(self, serializer):
        review = self.get_object()
        if review.user != self.request.user:
            raise PermissionDenied("You cannot edit other users' reviews.")
        serializer.save()

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "User created successfully."}, status=201)


class GameListView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'game_id'
    lookup_url_kwarg = 'game_id'


class GameCreateView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ReviewDeleteView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'review_id'
    lookup_url_kwarg = 'review_id'

    def perform_destroy(self, instance):
        # Only allow users to delete their own reviews
        if instance.user != self.request.user:
            raise PermissionDenied("You cannot delete other users' reviews.")
        instance.delete()

# Review Views
class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game', 'user']


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    user = request.user
    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    }
    return Response(data)


def backend_home(request):
    return render(request, 'backend_home.html')


def view_groups(request):
    return HttpResponse("Groups Data Page")


def view_genres(request):
    return HttpResponse("Genres Data Page")


def view_user_games(request):
    return HttpResponse("User Games Data Page")


def view_users(request):
    return HttpResponse("Users Data Page")