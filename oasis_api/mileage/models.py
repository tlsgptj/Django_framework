from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Mileage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    mileage_earned = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.store_name} - {self.mileage_earned}"

