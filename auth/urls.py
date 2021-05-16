from django.urls import path
from auth.views import ObtainAuthToken, AuthTest

app_name = 'app_auth'

urlpatterns = [
    path('auth', ObtainAuthToken.as_view(), name='obtain-auth-token'),
    path('auth-test', AuthTest.as_view())
]
