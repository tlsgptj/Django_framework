from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['card_number', 'expiry_date', 'cardholder_name', 'cvv']

    def validate_card_number(self, value):
        if len(value) != 16 or not value.isdigit():
            raise serializers.ValidationError("Invalid card number")
        return value

    def validate_cvv(self, value):
        if len(value) != 3 or not value.isdigit():
            raise serializers.ValidationError("Invalid CVV")
        return value
