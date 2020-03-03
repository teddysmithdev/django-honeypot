# django-honeypot
Low-Interaction honeypot built in Django for SSH, Telnet, and ICMP. Honeypots are 3 seperate scripts that run in the background of Django using Celery + Redis.

Demo: http://www.djangohoney.com

## Motivation
I saw another honeypot [built in NodeJS](https://github.com/Shmakov/Honeypot) that I thought was fascinating, so I built my own version in Python.

## Features
- Ability to see intial data recieved from intial connection
- Celery + Redis make it suprisingly stable
- All logs are stored in seperate areas to see where connections are coming from
- Nice web interface to see attacks
- Easy to build. Django is a great framework for beginners.


