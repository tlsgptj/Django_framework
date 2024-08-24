from rest_framework import serializers
from .models import Gifticon, UserGifticon

class GifticonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gifticon
        fields = '__all__'

class UserGifticonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGifticon
        fields = '__all__'
