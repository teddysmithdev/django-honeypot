from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import ConnectionItem
from telnet.models import ConnectionItem as ConnectionTelnet



def home_page(request):
    ssh_count = ConnectionItem.objects.all().count()
    telnet_count = ConnectionTelnet.objects.all().count()
    context = {'ssh_count': ssh_count, 'telnet_count': telnet_count}
    return render(request, 'main.html', context)