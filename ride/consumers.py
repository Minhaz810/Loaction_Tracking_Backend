from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Driver
from asgiref.sync import sync_to_async
import json

class DriverStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("driver_status", self.channel_name)
        await self.accept()
        await self.send_driver_status_data()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("driver_status", self.channel_name)

    async def send_driver_status_data(self, event=None):
        driver_status_data = {}

        for status, _ in Driver.STATUS_CHOICES:
            count = await sync_to_async(Driver.objects.filter(status=status).count)()
            drivers = await sync_to_async(list)(
                Driver.objects.filter(status=status).values("latitude", "longitude")
            )
            driver_status_data[status] = {
                "count": count,
                "coordinates": drivers
            }

        await self.send(text_data=json.dumps({"driver_status_data": driver_status_data}))
