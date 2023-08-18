from django.conf.urls import url
from rest_framework import routers

from apps.message import views

router = routers.DefaultRouter()
router.register("v1/message", views.MessageViewSet, basename="message")
urlpatterns = router.urls
