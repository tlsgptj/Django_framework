from django.db import models

class Card(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expiry_date = models.CharField(max_length=5)
    cardholder_name = models.CharField(max_length=100)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.cardholder_name} - {self.card_number}"


