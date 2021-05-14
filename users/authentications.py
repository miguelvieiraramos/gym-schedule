from rest_framework.authentication import TokenAuthentication


class AppAuthentication(TokenAuthentication):

    def authenticate(self, request):
        try:
            credentials = super().authenticate(request)

            if not credentials:
                return None

            return credentials
        except Exception:
            return None
