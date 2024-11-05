from django.db import models
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Driver(models.Model):
    user = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,null=False,blank=False,on_delete=models.CASCADE)

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('way_to_pickup', 'Way to Pickup'),
        ('reached_pickup', 'Reached Pickup'),
        ('way_to_dropoff', 'Way to Dropoff'),
        ('on_ride', 'On Ride'),
    ]

    
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=Driver)
def driver_status_changed(sender, instance, **kwargs):
    instance.refresh_from_db()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "driver_status",
        {
            "type": "send_driver_status_data",
        },
    )