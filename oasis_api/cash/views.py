from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from .utils import process_payment  # 또는 services에서 import

class PaymentView(APIView):

    def post(self, request):
        user = request.user
        amount = request.data.get('amount')

        try:
            payment = process_payment(user, amount)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

