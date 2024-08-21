from django.urls import path
from .views import register_card

urlpatterns = [
    path('register_card/', register_card, name='register_card'),
]
