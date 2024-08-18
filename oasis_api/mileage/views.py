from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Mileage
from .serializers import MileageSerializer

class MileageListView(generics.ListAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

