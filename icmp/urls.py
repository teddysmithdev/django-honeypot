from django.urls import path
from .views import icmp_page


urlpatterns = [
    path('icmp/', icmp_page),
]