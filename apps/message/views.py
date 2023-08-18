from rest_framework import status
from rest_framework.response import Response
from apps.core.model_view_set import BaseModelViewSet
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice


class MessageViewSet(BaseModelViewSet):
    def list(self, request, *args, **kwargs):
        data = {"token": "token", "user": "UserAccountSerializer"}
        response = Response(data=data)
        return response

    def create(self, request, *args, **kwargs):
        device = FCMDevice.objects.all().first()
        message = Message(
            data={"title": "Mario", "body": "great match!", "Room": "PortugalVSDenmark"},
        )
        try:
            device.send_message(message)
            data = {"message": "Message sent successfully"}
            response = Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {"error": str(e)}
            response = Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response
