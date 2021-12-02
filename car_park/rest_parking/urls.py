from django.urls import path
from . import views

urlpatterns = [
    path('drivers/driver/', views.DriversListView.as_view()),
    path('drivers/driver/<int:driver_id>/', views.DriverByIdListView.as_view()),
    path('vehicles/vehicle/', views.VehiclesListView.as_view()),
    path('vehicles/vehicle/<int:vehicle_id>/', views.VehicleCRUDView.as_view()),
    path('vehicles/set_driver/<int:vehicle_id>/', views.VehicleDriverSetView.as_view()),
]
