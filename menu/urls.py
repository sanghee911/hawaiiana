from django.conf.urls import url
from .views import (
    nigiri,
    roll,
    donburi,
    others,
)

urlpatterns = [
    url(r'^nigiri/$', nigiri, name='nigiri'),
    url(r'^roll/$', roll, name='roll'),
    url(r'^donburi/$', donburi, name='donburi'),
    url(r'^others/$', others, name='others'),
]