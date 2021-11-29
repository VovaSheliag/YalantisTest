from rest_framework import serializers
from .models import Driver, Vehicle


class DriversListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

