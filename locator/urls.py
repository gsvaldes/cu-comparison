from django.conf.urls import url, include
from rest_framework import routers

from locator.views import *

router = routers.DefaultRouter()
router.register(r'business', BusinessViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),
]