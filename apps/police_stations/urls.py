

from django.urls import path
from .views import  *


urlpatterns = [
    path('', manage_police_stations, name="police-stations"),
    path('add', add_police_station, name="add"),
    path('edit/<int:pk>', edit_police_station, name="edit"),
    path('delete/<int:pk>', delete_police_station, name="delete"),
]
