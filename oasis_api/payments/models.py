from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.card_number[-4:]}"

