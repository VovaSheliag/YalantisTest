from .models import Driver, Vehicle
import datetime
from .serializers import DriversListSerializer, VehicleListSerializer


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


def get_vehicles(request):
    if 'with_drivers' in request.GET:
        if request.GET['with_drivers'] == 'yes':
            return Vehicle.objects.filter(driver_id=not None)
        return Vehicle.objects.filter(driver_id=None)
    return Vehicle.objects.all()


def get_driver_by_id(driver_id):
    return Driver.objects.filter(id=driver_id)


def get_vehicle_by_id(vehicle_id):
    return Vehicle.objects.filter(id=vehicle_id)
