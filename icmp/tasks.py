from __future__ import absolute_import, unicode_literals
import time
import socket
import os
from .models import ConnectionItem
from celery.decorators import task


@task(name="runicmp")
def main():
  s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
  s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
  while 1:
    data, addr = s.recvfrom(1508)
    print("Packet from %r: %r" % (addr,data))
    log = ConnectionItem(address=addr, data=data)
    log.save