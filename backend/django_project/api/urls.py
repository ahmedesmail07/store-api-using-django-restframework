from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

"""
from .views import api_home , You can import it like this but 
above u can import all the views in single line of code

"""

urlpatterns = [
    path("auth/", obtain_auth_token),
    path("", views.api_home),
]  # api_home >> This View will shown as a JSON Format at : localhost:8000/api
