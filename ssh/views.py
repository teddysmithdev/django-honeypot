from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import ConnectionItem
from telnet.models import ConnectionItem as ConnectionTelnet
from icmp.models import ConnectionItem as ConnectionICMP




def home_page(request):
    ssh_count = ConnectionItem.objects.all().count()
    telnet_count = ConnectionTelnet.objects.all().count()
    icmp_count = ConnectionICMP.objects.all().count()
    context = {'ssh_count': ssh_count, 'telnet_count': telnet_count, 'icmp_count': icmp_count}
    return render(request, 'main.html', context)

def ssh_page(request):
    ssh_logs = ConnectionItem.objects.all()
    return render(request, 'ssh.html', {'ssh_logs': ssh_logs})