import datetime

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
