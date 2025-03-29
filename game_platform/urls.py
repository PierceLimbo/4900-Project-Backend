from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('games.urls')),  # backend homepage
    path('admin/', admin.site.urls),  # admin panel
    path('api/', include('games.urls')),  # optional for API routes
]
