import json

from channels.generic.websocket import WebsocketConsumer


# Consumers are equivalent to Django views for async apps.
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Accept connection
        self.accept()

    def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
