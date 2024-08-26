from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    availableLocalCurrency = models.CharField(max_length=255, default="N/A")
    cityName = models.CharField(max_length=255, default="Unknown")
    districtName = models.CharField(max_length=255)
    streetAddress = models.CharField(max_length=255)

    def __str__(self):
        return self.name

