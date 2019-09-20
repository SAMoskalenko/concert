import json
from django.db.models import Sum
from django.db.models import signals
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import channels.layers

from donat.models import DonationsData


class ReleaseConsumer(WebsocketConsumer):
    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            # self.room_group_name,
            'release_data',
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            'release_data',
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            'release_data',
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            # self.room_group_name,
            'release_data',
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))

    @staticmethod
    @receiver(signals.post_save, sender=DonationsData)
    def order_offer_observer(sender, instance, **kwargs):
        message = DonationsData.objects.aggregate(Sum('summ'))['summ__sum']
        layer = channels.layers.get_channel_layer()
        async_to_sync(layer.group_send)('release_data', {
            'type': 'chat_message',
            'message': message,
        })
