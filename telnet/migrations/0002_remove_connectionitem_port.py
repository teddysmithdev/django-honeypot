# Generated by Django 3.0.3 on 2020-03-02 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telnet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectionitem',
            name='port',
        ),
    ]
