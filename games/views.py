from django.shortcuts import render

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
