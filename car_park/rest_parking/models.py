from django.db import models
from .validators import plate_number_validator


class Driver(models.Model):
    """
    Model to save info about driver
    """
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Vehicle(models.Model):
    """
    Model to save info about drivers vehicle
    """
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=128)
    plate_number = models.CharField(max_length=10, unique=True,             # Validate format example "AA 1234 OO"
                                    validators=[plate_number_validator])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return f'{self.model} | {self.plate_number}'




