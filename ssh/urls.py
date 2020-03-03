from django.urls import path
from .views import home_page, ssh_page


urlpatterns = [
    path('', home_page),
    path('ssh/', ssh_page),
]