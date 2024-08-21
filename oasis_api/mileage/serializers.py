from rest_framework import serializers
from .models import Mileage

class MileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mileage
        fields = ['points', 'date', 'description']


