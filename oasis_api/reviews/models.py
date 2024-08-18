from django.db import models
from django.contrib.auth import get_user_model
from store.models import Store

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.store.name} - {self.rating}"

