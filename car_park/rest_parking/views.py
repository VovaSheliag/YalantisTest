from rest_framework import generics
from rest_framework.views import APIView, Response
from .services import *
from .serializers import DriversListSerializer, VehicleListSerializer


class DriversListView(APIView):
    """
    Get all drivers list, or get driver by date if in request we have "created_at__gte" - means get drivers created
    greater than equal inputed date or "created_at__lte" - means get drivers created less than equal inputed date
    """
    def get(self, request, *args, **kwargs):
        drivers_list = get_drivers_list(request)
        if not drivers_list:
            return Response(f'Error: No drivers yet')
        drivers_list_serializer = DriversListSerializer(drivers_list, many=True)
        return Response(drivers_list_serializer.data)

    def post(self, request, *args, **kwargs):
        driver_create_serializer = DriversListSerializer(request.data, many=True)
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
            return Response(f'Error: No driver with id={driver_id}')
        driver_serializer = DriversListSerializer(driver, many=True)
        return Response(driver_serializer.data)

    def put(self, request, driver_id):
        data = request.data
        driver = get_driver_by_id(driver_id)
        driver_serializer = DriversListSerializer(data=data, many=True)
        if driver_serializer.is_valid():
            driver.first_name = data[0]['first_name']
            driver.last_name = data[0]['last_name']
            driver.save()
            return Response(f"Success driver was updated")
        return Response(driver_serializer.errors, status=201)

    def delete(self, request, driver_id):
        driver = get_driver_by_id(driver_id)
        return delete_object_by_id(driver, driver_id)


class VehiclesListView(APIView):
    def get(self, request):
        vehicles = get_vehicles(request)
        if not vehicles:
            return Response('No vehicles yet')
        vehicles_serializer = VehicleListSerializer(vehicles, many=True)
        return Response(vehicles_serializer.data)

    def post(self, request, *args, **kwargs):
        new_vehicle = VehicleListSerializer(data=request.data, many=True)
        if new_vehicle.is_valid():
            new_vehicle.save()
            return Response(f"Success: vehicle {new_vehicle.data[0]['model']} | "
                            f"{new_vehicle.data[0]['plate_number']} was created")
        return Response(new_vehicle.errors, status=201)


class VehicleCRUDView(APIView):
    def get(self, request, vehicle_id):
        vehicle = get_vehicle_by_id(vehicle_id)
        if not vehicle:
            return Response(f'Error: No vehicle with id={vehicle_id}')
        vehicle_serializer = VehicleListSerializer(vehicle, many=True)
        return Response(vehicle_serializer.data)

    def put(self, request, vehicle_id):
        data = request.data
        vehicle = get_vehicle_by_id(vehicle_id)
        vehicle.update(make=data[0]['make'], model=data[0]['model'], plate_number=data[0]['plate_number'])
        return Response(f"Success: vehicle with id={vehicle_id} was updated")

    def delete(self, request, vehicle_id):
        vehicle = get_vehicle_by_id(vehicle_id)
        return delete_object_by_id(vehicle, vehicle_id)


class VehicleDriverSetView(APIView):
    def post(self, request, vehicle_id):
        vehicle = Vehicle.objects.filter(id=vehicle_id)
        print(vehicle)
        driver_id = request.data[0]['driver_id']
        if not vehicle:
            return Response(f'Error: No vehicle with id={vehicle_id}')
        driver = Driver.objects.filter(id=driver_id)
        if not driver and driver_id:
            return Response(f'Error: No driver with id={driver_id}')
        set_driver_in_vehicle(vehicle, driver_id)
        return Response(f'Success: driver with id={driver_id} was set in vehicle with id={vehicle_id}')

