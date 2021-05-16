from django.urls import path, include


urlpatterns = [
    path('', include('users.urls', namespace='users')),
    path('', include('auth.urls', namespace='auth')),
]
