from django.conf.urls import url
from .views import location

urlpatterns = [
    url(r'^$', location, name='location'),
]