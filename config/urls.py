from django.urls import path, include


urlpatterns = [
    path('', include('gym_schedule.users.urls', namespace='users')),
    path('', include('gym_schedule.auth.urls', namespace='auth')),
]
