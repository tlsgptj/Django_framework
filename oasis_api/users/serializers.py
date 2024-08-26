from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'password')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError('Email and password are required')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('No active account found with the given credentials')

        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect password')

        if not user.is_active:
            raise serializers.ValidationError('This account is inactive')

        # 기존의 TokenObtainPairSerializer의 validate 메소드를 호출
        data = super().validate(attrs)

        data['user'] = {
            'id': user.id,
            'nickname': user.nickname,
            'email': user.email,
        }

        return data
