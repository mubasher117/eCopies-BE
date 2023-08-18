from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.core.model_view_set import BaseModelViewSet


class MessageViewSet(BaseModelViewSet):
    def list(self, request, *args, **kwargs):
        data = {"token": "token", "user": "UserAccountSerializer"}
        response = Response(data=data)
        return response

    def create(self, request, *args, **kwargs):
        renderer = JSONRenderer()
        data = renderer.render({"message": "SUCCESS."})

        return HttpResponse(data, "application/json", status=status.HTTP_200_OK)
