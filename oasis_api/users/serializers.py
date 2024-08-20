from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'nickname')

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'password')

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        return data_dict

    def save(self, request):
        user = super().save(request)
        user.nickname = self.validated_data.get('nickname', '')
        user.save()
        return user

class CustomTokenSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('token', 'user')

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return str(refresh.access_token)

    def to_representation(self, instance):
        representation = {
            'token': self.get_token(instance),
            'user': {
                'id': instance.id,
                'nickname': instance.nickname,
                'email': instance.email,
            }
        }
        return representation

