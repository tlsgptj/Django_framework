import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from store.models import Store

class Command(BaseCommand):
    help = 'Load shop data from a local CSV file into the database'

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(settings.BASE_DIR, 'store', 'management', 'commands', 'store_data.csv')

        try:
            with open(csv_path, mode='r', encoding='cp949') as file:
                reader = csv.DictReader(file)

                Store.objects.all().delete()

                for row in reader:
                    latitude = row.get('latitude', None)
                    longitude = row.get('longitude', None)

                    # 빈 값 처리
                    if not latitude or latitude.strip() == "":
                        latitude = None  # 또는 0.0, 기본값을 원하는 대로 설정
                    if not longitude or longitude.strip() == "":
                        longitude = None  # 또는 0.0, 기본값을 원하는 대로 설정

                    Store.objects.create(
                        name=row['name'],
                        availableLocalCurrency=row['availableLocalCurrency'],
                        cityName=row['cityName'],
                        districtName=row['districtName'],
                        streetAddress=row['streetAddress'],
                        latitude=latitude,
                        longitude=longitude
                    )

            self.stdout.write(self.style.SUCCESS('Successfully loaded shop data into the database'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {csv_path}'))
        except UnicodeDecodeError as e:
            self.stdout.write(self.style.ERROR(f'Encoding error: {e}'))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f'Key error: {e} - Check CSV header names'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
