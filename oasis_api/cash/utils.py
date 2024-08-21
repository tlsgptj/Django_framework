from django.db import transaction
from .models import Payment, Mileage

def process_payment(user, amount):
    try:
        with transaction.atomic():
            # 결제 기록 생성
            payment = Payment.objects.create(user=user, amount=amount, status="completed")

            # 마일리지 적립
            mileage_points = calculate_mileage(amount)  # 예: 결제 금액의 10%를 적립
            Mileage.objects.create(user=user, points=mileage_points, description="Payment Mileage")

            return payment
    except Exception as e:
        raise e

def calculate_mileage(amount):
    return amount * 0.10
