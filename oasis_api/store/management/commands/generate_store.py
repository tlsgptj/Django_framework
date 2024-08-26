import json
import os
from django.core.management.base import BaseCommand
from store.models import Store

class Command(BaseCommand):
    help = 'Load shop data from a local JSON file into the database'

    def handle(self, *args, **kwargs):
        # 로컬 파일 경로 설정
        json_file_path = os.path.join('store', 'management', 'commands', 'store_data.json')

        # JSON 파일 읽기
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)

        # 기존 데이터 삭제 (옵션)
        Store.objects.all().delete()

        # JSON 데이터를 Django 모델에 삽입
        for item in data:
            latitude = item.get('latitude')
            longitude = item.get('longitude')

            # 빈 문자열을 None으로 처리
            if latitude == "":
                latitude = None
            if longitude == "":
                longitude = None

            Store.objects.create(
                name=item['name'],
                availableLocalCurrency=item['availableLocalCurrency'],
                cityName=item['cityName'],
                districtName=item['districtName'],
                streetAddress=item['streetAddress'],
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded shop data from local JSON file'))

