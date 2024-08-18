from rest_framework import generics
from .models import Store
from .serializers import StoreSerializer

class StoreListView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

