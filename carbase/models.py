# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible  # Compatibility with Python 3
#from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

import reversion


@python_2_unicode_compatible
class CarMake(models.Model):
    name = models.CharField(max_length=30)
    comments = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('carmake_detail', args=[str(self.id)])

    def __str__(self):
        return "%s" % self.name

reversion.register(CarMake)


@python_2_unicode_compatible
class CarModel(models.Model):
    make = models.ForeignKey(CarMake)
    model = models.CharField(max_length=30)
    comments = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('carmodel_detail', args=[str(self.id)])

    def __str__(self):
        return "%s %s" % (self.make, self.model)

reversion.register(CarModel)