from django.urls import path
from .views import telnet_page


urlpatterns = [
    path('telnet/', telnet_page)
]