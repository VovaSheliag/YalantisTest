from django.urls import path
from . import views

urlpatterns = [
    path('drivers/driver/', views.DriversListView.as_view()),
]
