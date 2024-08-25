from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import CustomUser


class Gifticon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class UserGifticon(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gifticon = models.ForeignKey(Gifticon, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.gifticon.name}'
