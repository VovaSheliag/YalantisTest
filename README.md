# REST API for car park with drivers

This is a bare-bones example of application providing a REST API to working with Drivers 
and Vehicles models.

### Technical stack 
+ Python version - 3.9
+ Main framework - Django 
+ REST api - django rest framework 
+ Database - SQLite

### Main functionality
This project provides you possibility to get, post, update and delete information about drivers
and vehicles. You can filter drivers and vehicles lists by some parameters as well.

### Endpoint`s

Driver:
+ GET /drivers/driver/ - output drivers list
+ GET /drivers/driver/?created_at__gte=10-11-2021 - output of the list of drivers created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - output of the list of drivers created before 16-11-2021
+ GET /drivers/driver/<driver_id>/ - obtaining information on a particular driver
+ POST /drivers/driver/ - create new driver
  + Required fields:
  

    {
        "first_name": str,
        "last_name": str
    }
+ UPDATE /drivers/driver/<driver_id>/ - update driver`s info
  + Required fields:
  

    {
        "first_name": str,
        "last_name": str
    }
+ DELETE /drivers/driver/<driver_id>/ - delete driver

Vehicle:
+ GET /vehicles/vehicle/ - output vehicles list
+ GET /vehicles/vehicle/?with_drivers=yes - output of the list of cars with drivers
+ GET /vehicles/vehicle/?with_drivers=no - output of the list of cars without drivers
+ GET /vehicles/vehicle/<vehicle_id> - obtaining information on a specific machine
+ POST /vehicles/vehicle/ - create new vehicle
  + Required fields:
  

    {
        "driver_id": int/null,
        "make": str,
        "model": str,
        "plate_number": str
    }
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - update vehicle`s info 
  + Required fields:
  

    {
        "make": str,
        "model": str,
        "plate_number": str 
    }
+ POST /vehicles/set_driver/<vehicle_id>/ - put the driver in the car / get the driver out of the car
  + Required fields:
  

    {
        "driver_id": int/null
    }
+ DELETE /vehicles/vehicle/<vehicle_id>/ - delete vehicle