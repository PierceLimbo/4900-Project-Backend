from django.urls import path
from .views import backend_home

urlpatterns = [
    path('', backend_home, name='backend-home'),
    # other API routes
]
