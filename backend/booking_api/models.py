from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.


# Custom User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["username"]











class Room(models.Model):

    ROOM_TYPES = [
        ("suite", "Suite"),
        ("deluxe", "Deluxe"),
        ("standard", "Standard"),
    ]

    CURRENCY_TYPES = [
        ("usd", "USD"),
        ("eur", "EUR"),
        ("naira", "Naira"),
    ]
    name = models.CharField(max_length=100, blank=True, default="")
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, default="standard")
    price_per_night = models.IntegerField(default=150)
    currency = models.CharField(max_length=10, choices=CURRENCY_TYPES, default="usd")
    max_occupancy = models.IntegerField(default=1)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.name} - {self.room_type}"


# Roomimage
class RoomImage(models.Model):
    image = models.ImageField(upload_to="room_images/%Y/%m/%d/", blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    room = models.ForeignKey("Room", related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption or f"Image for {self.room.name}"


# Occupied date
class OccupiedDate(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="occupied_dates", on_delete=models.CASCADE
    )  # OR SETTINGS.AUTH_USER_MODEL
    room = models.ForeignKey(
        Room, related_name="occupied_dates", on_delete=models.CASCADE
    )
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.room.name} - {self.date}"




