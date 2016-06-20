from __future__ import unicode_literals

from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __unicode__(self):
        return self.name


class Nigiri(MenuItem):
    pass


class Bento(MenuItem):
    pass

