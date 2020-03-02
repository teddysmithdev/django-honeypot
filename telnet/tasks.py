from __future__ import absolute_import, unicode_literals
import random
import time
import socket
import os
from .models import ConnectionItem
from celery.decorators import task

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')



@task(name="runtelnet")
def main():
	print('Starting honeypot!')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('0.0.0.0', 21))
	s.listen(100)
	while True:
		(insock, address) = s.accept()
		print('Connection from: %s:%d' % (address[0], address[1]))
		try:
			insock.send('Telnet login: '.encode())
			data = insock.recv(1024)
			log = ConnectionItem(address=address[0], port=address[1], data=data)
			log.save()
			insock.close()
		except socket.error as e:
			print('aaaaaaa')
		else:
			print('bbbbbbb')