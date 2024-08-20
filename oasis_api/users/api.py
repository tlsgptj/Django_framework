from rest_framework import generics, permissions
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView

class LogoutAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=200)

class UserDetailAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class RegisterAPI(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
