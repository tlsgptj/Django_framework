from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .utils import verify_email_verification_token

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        nickname = request.data.get('nickname') 

        if not email or not password or not nickname:
            return Response({"detail": "Email, password, and nickname are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"detail": "A user with that email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(nickname=nickname).exists():
            return Response({"detail": "A user with that nickname already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(email=email, password=password, nickname=nickname)
        user.is_active = False
        user.save()

        return Response({"detail": "Please check your email to verify your account."}, status=status.HTTP_201_CREATED)

class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        user_pk = verify_email_verification_token(token)
        if user_pk:
            user = User.objects.get(pk=user_pk)
            user.is_active = True
            user.save()
            return Response({"detail": "Your email has been verified successfully. You can now log in."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Verification link is invalid or has expired."}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except (AttributeError, Token.DoesNotExist):
            return Response({"detail": "Invalid token or user not logged in."}, status=status.HTTP_400_BAD_REQUEST)

