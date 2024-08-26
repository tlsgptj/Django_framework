from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    availableLocalCurrency = models.CharField(max_length=255, default="N/A")
    cityName = models.CharField(max_length=255, default="Unknown")
    districtName = models.CharField(max_length=255)
    streetAddress = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

