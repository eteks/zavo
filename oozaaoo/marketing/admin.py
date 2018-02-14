# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Marketing

# from forms import MarketingForm,accomodationTypeForm,combinedForm
from forms import MarketingForm
# from forms import MarketingForm

# Register your models here.
class MarketingAdmin(admin.ModelAdmin):
	# model = Marketing
	# list_display = ('get_package','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','notes')
	# form = MarketingForm

	# def get_package(self, obj):
	# 	return obj.packageName
	# get_package.short_description = 'Package Name'
	pass

admin.site.register(Marketing,MarketingAdmin)


