import random
import string
from datetime import datetime
from django.core.management.base import BaseCommand
from users.models import CustomUser
from gift.models import Gifticon, UserGifticon  # gift를 실제 앱 이름으로 변경

class Command(BaseCommand):
    help = 'Delete existing dummy data and generate new 30 dummy gifticon and user gifticon data'

    def generate_unique_barcode(self):
        """고유한 바코드를 생성하는 함수"""
        while True:
            barcode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
            if not UserGifticon.objects.filter(barcode=barcode).exists():
                return barcode

    def handle(self, *args, **kwargs):
        # 기존 데이터 삭제
        UserGifticon.objects.all().delete()
        Gifticon.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Existing dummy data deleted.'))

        users = CustomUser.objects.all()

        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create some users first.'))
            return

        for i in range(1, 31):
            gifticon_name = f'Gifticon #{i}'
            gifticon_description = f'Description for {gifticon_name}'
            gifticon_price = round(random.uniform(10.0, 100.0), 2)
            gifticon_image_url = f'https://dummyimage.com/600x400/000/fff&text={gifticon_name}'

            gifticon = Gifticon.objects.create(
                name=gifticon_name,
                description=gifticon_description,
                price=gifticon_price,
                image_url=gifticon_image_url
            )

            user = random.choice(users)
            barcode = self.generate_unique_barcode()

            UserGifticon.objects.create(
                user=user,
                gifticon=gifticon,
                barcode=barcode,
                is_used=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated 30 new dummy gifticon and user gifticon data.'))
