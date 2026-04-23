from django.db import models
from django.contrib.auth.models import User

class Ambulance(models.Model):
    name = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=50, unique=True)

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return f"{self.name} ({self.status})"


class Booking(models.Model):
    EMERGENCY_LEVELS = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ambulance = models.ForeignKey(Ambulance, on_delete=models.SET_NULL, null=True, blank=True)

    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)

    emergency_level = models.CharField(max_length=10, choices=EMERGENCY_LEVELS)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.emergency_level} - {self.created_at}"