from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import authentication, permissions


# Basic authentication endpoints
class LoginView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request, format=None) -> Response:
        data = request.data
        user = authenticate(username=data["username"], password=data["password"])

        if user:
            if user.is_active:
                if Token.objects.filter(user=user).exists():
                    user.auth_token.delete()
                token = Token.objects.create(user=user)
                return Response(data={"token": token.key}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)


class logoutView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request) -> Response:
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
