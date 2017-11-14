# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import TourPackage

# Register your models here.
class TourPackageAdmin(admin.ModelAdmin):
	model = TourPackage
	list_display = ('get_package','contactAddress','contactMobile','contactMail','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','accomodationType','accomodationStar','modeOfTransport','notes','breakfast','lunch','dinner')

	def get_package(self, obj):
		return obj.TourPackage.packageName
	get_package.short_description = 'Package Name'

admin.site.register(TourPackage,TourPackageAdmin)
