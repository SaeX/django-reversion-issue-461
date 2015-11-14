# -*- encoding: utf-8 -*-

from django.contrib import admin

import reversion

from .models import CarMake, CarModel


admin.site.register(CarMake, reversion.VersionAdmin)
admin.site.register(CarModel, reversion.VersionAdmin)