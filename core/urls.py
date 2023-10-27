
from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("accounts/", include("apps.authentication.urls")), # Auth routes - login / register

    # Police Stations
    path("police-stations/", include("apps.police_stations.urls")),
     
    # Police 
    path("police/", include("apps.police.urls")),

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]
