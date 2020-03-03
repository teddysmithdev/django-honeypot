from django.shortcuts import render
from .models import ConnectionItem
# Create your views here.



def telnet_page(request):
    telnet_logs = ConnectionItem.objects.all()
    return render(request, 'telnet.html', {'telnet_logs': telnet_logs})