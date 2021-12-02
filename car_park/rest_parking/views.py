from .serializers import DriversListSerializer, VehicleListSerializer
from .models import Driver, Vehicle
from rest_framework import generics
from rest_framework.views import APIView, Response
from .services import *


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
    Get, update, delete  driver from model by id
    """
    def get(self, request, driver_id):
        driver = get_driver_by_id(driver_id)
        if not driver:
            return Response(f'No driver with id={driver_id}')
        driver_serializer = DriversListSerializer(driver, many=True)
        return Response(driver_serializer.data)

    def put(self, request, driver_id):
        data = request.data
        driver = get_driver_by_id(driver_id)
        driver_serializer = DriversListSerializer(data=request.data, many=True)
        if driver_serializer.is_valid():
            driver.first_name = data[0]['first_name']
            driver.last_name = data[0]['last_name']
            driver.save()
            return Response(f"Success driver was updated")
        return Response(driver_serializer.errors, status=201)

    def delete(self, request, driver_id):
        driver = get_driver_by_id(driver_id)
        if not driver:
            return Response(f"No driver with id={driver_id}")
        driver.delete()
        return Response(f"Success: driver with id={driver_id} was deleted")


class DriverPostView(generics.CreateAPIView):
    serializer_class = DriversListSerializer


class VehiclesListView(APIView):
    def get(self, request):
        vehicles = get_vehicles(request)
        if not vehicles:
            return Response('No such vehicles in database')
        vehicles_serializer = VehicleListSerializer(vehicles, many=True)
        return Response(vehicles_serializer.data)


