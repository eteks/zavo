# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.
class TourpackageAdmin(admin.ModelAdmin):
	model = Tourpackage

admin.site.register(Tourpackage, TourpackageAdmin)