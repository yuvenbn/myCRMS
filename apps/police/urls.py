

from django.urls import path
from .views import  *


urlpatterns = [
    path('', manage_police, name="police"),
    path('add', add_police, name="add"),
    path('edit/<int:pk>', edit_police, name="edit"),
]
