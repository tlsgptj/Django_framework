from rest_framework import viewsets
from .models import Gifticon
from .serializers import GifticonSerializer
from .models import UserGifticon
from .serializers import UserGifticonSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Gifticon, UserGifticon
import uuid

class GifticonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gifticon.objects.all()
    serializer_class = GifticonSerializer

class UserGifticonViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserGifticon.objects.filter(user=self.request.user)

    serializer_class = UserGifticonSerializer

@api_view(['POST'])
def purchase_gifticon(request):
    user = request.user
    gifticon_id = request.data.get('gifticon_id')
    gifticon = Gifticon.objects.get(id=gifticon_id)

    if user.mileage < gifticon.price:
        return Response({'error': 'Not enough mileage'}, status=status.HTTP_400_BAD_REQUEST)

    # 마일리지 차감
    user.mileage -= gifticon.price
    user.save()

    # 바코드 생성 및 저장
    barcode = str(uuid.uuid4())
    user_gifticon = UserGifticon.objects.create(
        user=user,
        gifticon=gifticon,
        barcode=barcode
    )

    return Response({'barcode': barcode}, status=status.HTTP_201_CREATED)
