# Generated by Django 3.0.3 on 2020-03-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssh', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectionitem',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='connectionitem',
            name='remote_port',
        ),
        migrations.AddField(
            model_name='connectionitem',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='connectionitem',
            name='data',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='connectionitem',
            name='port',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
