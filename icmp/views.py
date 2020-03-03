from django.shortcuts import render
from .models import ConnectionItem
# Create your views here.


def icmp_page(request):
    icmp_logs = ConnectionItem.objects.all()
    return render(request, 'icmp.html', {'icmp_logs': icmp_logs})