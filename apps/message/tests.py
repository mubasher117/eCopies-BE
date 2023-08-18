from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from apps.message.views import MessageViewSet
import jwt
import base64
from django.conf import settings
from apps.authentication.utils import JwtTokenGenerator

from django.contrib.auth import get_user_model

User = get_user_model()


class MessageViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = MessageViewSet.as_view({"get": "list", "post": "create"})
        self.url = "/messages/"
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token_generator = JwtTokenGenerator()
        self.auth_token = self.token_generator.get_token(self.user)

    def test_list(self):
        request = self.factory.get(
            self.url, HTTP_AUTHORIZATION="Bearer {}".format(self.auth_token)
        )
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "status": True,
                "code": 0,
                "message": None,
                "data": {"token": "token", "user": "UserAccountSerializer"},
            },
        )

    def test_create(self):
        request = self.factory.post(
            self.url, HTTP_AUTHORIZATION="Bearer {}".format(self.auth_token)
        )
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["data"]["token"],
            "token",
        )
