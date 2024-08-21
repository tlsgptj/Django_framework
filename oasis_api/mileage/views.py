from rest_framework import generics
from .models import Mileage
from .serializers import MileageSerializer

class MileageListView(generics.ListAPIView):
    serializer_class = MileageSerializer

    def get_queryset(self):
        return Mileage.objects.filter(user=self.request.user)



