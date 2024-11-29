from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)  # 샵 이름
    availableLocalCurrency = models.CharField(max_length=50)  # 사용 가능한 지역 화폐
    cityName = models.CharField(max_length=50)  # 도시 이름
    districtName = models.CharField(max_length=50)  # 구 이름
    streetAddress = models.TextField()  # 상세 주소
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # 위도
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
