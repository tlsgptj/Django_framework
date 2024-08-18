from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from mileage.models import Mileage
from store.models import Store

User = get_user_model()  # get_user_model()을 사용하여 User 모델 가져오기

class Command(BaseCommand):
    help = "Load initial data into the database"

    def handle(self, *args, **kwargs):
        # 유저 생성
        user = User.objects.create_user(username="testuser", email="test@example.com", password="password")
        
        # 마일리지 데이터 생성
        Mileage.objects.create(user=user, store_name="Store 1", amount=100.00, mileage_earned=10.00)
        
        # 가맹점 데이터 생성
        Store.objects.create(name="Store 1", address="123 Main St", latitude=37.7749, longitude=-122.4194)

        self.stdout.write(self.style.SUCCESS("Initial data loaded successfully"))
