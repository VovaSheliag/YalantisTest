import datetime

from django.shortcuts import get_list_or_404

from .serializers import DriversListSerializer, VehicleListSerializer
from .models import Driver, Vehicle
from rest_framework import generics
from rest_framework.views import APIView, Response


class DriversListView(APIView):
    """
    Get all drivers list, or get driver by date if in request we have "created_at__gte" - means get drivers created
    greater than equal inputed date or "created_at__lte" - means get drivers created less than equal inputed date
    """
    def get(self, request, *args, **kwargs):
        drivers_list = get_drivers_list(request)
        drivers_list_serializer = DriversListSerializer(drivers_list, many=True)
        return Response(drivers_list_serializer.data)

    def post(self, request, *args, **kwargs):
        driver_create_serializer = DriversListSerializer(data=request.data)
        if driver_create_serializer.is_valid():
            driver_create_serializer.save()
            return Response(f"Success {driver_create_serializer.data['first_name']} "
                            f"{driver_create_serializer.data['last_name']}"
                            f"was created")
        return Response(driver_create_serializer.errors, status=201)


class DriverByIdListView(APIView):
    """
    Get driver from model by id
    """
    def get(self, driver_id):
        driver = Driver.objects.filter(id=driver_id)
        if not driver:
            return Response('No driver with that id')
        driver_serializer = DriversListSerializer(driver, many=True)
        return Response(driver_serializer.data)


class DriverPostView(generics.CreateAPIView):
    serializer_class = DriversListSerializer



def get_drivers_list(request):
    if 'created_at__gte' in request.GET:
        date = get_splited_date(request.GET['created_at__gte'], '-')
        # Get all drivers which were created gte request.created_at date
        drivers_list = Driver.objects.filter(created_at__gte=datetime.datetime(date[2],
                                                                               date[1], date[0]))
    elif 'created_at__lte' in request.GET:
        date = get_splited_date(request.GET['created_at__lte'], '-')
        # Get all drivers which were created lte request.created_at date
        drivers_list = Driver.objects.filter(created_at__lte=datetime.datetime(date[2],
                                                                               date[1], date[0]))
    else:
        drivers_list = Driver.objects.all()
    return drivers_list


def get_splited_date(date, symbol):
    """First argument is a date, and a second is a symbol which is used to split"""
    return [int(x) for x in date.split(symbol)]
