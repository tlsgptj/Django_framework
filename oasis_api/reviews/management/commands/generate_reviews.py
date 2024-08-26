import json
import os
from django.core.management.base import BaseCommand
from reviews.models import Review
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Load review data from a local JSON file into the database'

    def handle(self, *args, **kwargs):
        # 로컬 파일 경로 설정
        json_file_path = os.path.join('reviews', 'management', 'commands', 'reviews.json')

        # JSON 파일 읽기
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)

        # 기존 데이터 삭제 (옵션)
        Review.objects.all().delete()

        # JSON 데이터를 Django 모델에 삽입
        for item in data:
            user_id = item.get('user_id')
            title = item.get('title')
            content = item.get('content')
            rating = item.get('rating')
            created_at = item.get('created_at')

            # ForeignKey로 연결된 User 객체 가져오기
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Skipping review due to missing user with ID {user_id}"))
                continue

            # Review 객체 생성
            Review.objects.create(
                user=user,
                title=title,
                content=content,
                rating=rating,
                created_at=created_at
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded review data from local JSON file'))
