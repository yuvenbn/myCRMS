

from django.urls import path
from .views import  *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("landing-page/", landing_page_view, name="landing-page"),
    path('register/level=<str:user_level>', register_view, name="register"),
    path('login/level=<str:user_level>', login_view, name="login"),
    path('police-login', police_login_view, name="police-login"),
    path("logout", LogoutView.as_view(), name="logout"),
    
    #management
    path('edit-profile', edit_profile_view, name="edit-profile"),
    path('change-password', change_password, name="change-password"), 


]
