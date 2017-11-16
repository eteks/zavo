# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Marketing

# Register your models here.
class MarketingAdmin(admin.ModelAdmin):
	model = Marketing
	list_display = ('get_package','contactAddress','contactMobile','contactMail','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','accomodationType','accomodationStar','modeOfTransport','notes','breakfast','lunch','dinner')

	def get_package(self, obj):
		return obj.packageName
	get_package.short_description = 'Package Name'

admin.site.register(Marketing,MarketingAdmin)
