from django.conf.urls import url
from django.urls import include


urlpatterns = [
    url('', include('apps.authentication.urls')),
    url('', include('apps.user.urls')),
    url('', include('apps.message.urls')),
]
