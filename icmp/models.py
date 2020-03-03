from django.db import models

# Create your models here.
class ConnectionItem(models.Model):
    address         = models.CharField(max_length=100, null=True, blank=True)
    port            = models.CharField(max_length=100, null=True, blank=True)  
    data            = models.CharField(max_length=120, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address