from django.urls import path
from . import views

urlpatterns = [
    path('drivers/driver/', views.DriversListView.as_view()),
    path('drivers/driver/<int:driver_id>/', views.DriverByIdListView.as_view()),
]
