import requests
import json
from requests.exceptions import HTTPError, Timeout, RequestException
from django.core.management.base import BaseCommand
from store.models import Store  # your_app을 실제 앱 이름으로 변경

class Command(BaseCommand):
    help = 'Download JSON file and load shop data into the database'

    def handle(self, *args, **kwargs):
        # 외부 JSON 파일 URL
        json_url = 'https://example.com/shop_data.json'

        # JSON 파일 다운로드
        response = requests.get(json_url)
        response.raise_for_status()  # 요청이 성공적으로 이루어졌는지 확인

        # JSON 데이터를 메모리에서 읽기
        data = response.json()

        # 기존 데이터 삭제 (옵션)
        Shop.objects.all().delete()

        # JSON 데이터를 Django 모델에 삽입
        for item in data:
            Store.objects.create(
                name=item['name'],
                availableLocalCurrency=item['availableLocalCurrency'],
                cityName=item['cityName'],
                districtName=item['districtName'],
                streetAddress=item['streetAddress'],
                latitude=item['latitude'],
                longitude=item['longitude']
            )

        self.stdout.write(self.style.SUCCESS('Successfully downloaded and loaded shop data into the database'))
