# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Marketing,accomodationTypeCreation,accomodationStarCreation,accomodationType,modeOfTransport,modeOfTransportCreation,transportTypeCreation

# from forms import MarketingForm,accomodationTypeForm,combinedForm
from forms import MarketingForm,accomodationTypeForm
# from forms import MarketingForm

# Register your models here.
class MarketingAdmin(admin.ModelAdmin):
	model = Marketing
	list_display = ('get_package','contactAddress','contactMobile','contactMail','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','notes','breakfast','lunch','dinner')
	form = MarketingForm

	def get_package(self, obj):
		return obj.packageName
	get_package.short_description = 'Package Name'

class accomodationTypeAdminCreation(admin.ModelAdmin):
	model = accomodationTypeCreation

class accomodationStarAdminCreation(admin.ModelAdmin):
	model = accomodationStarCreation

class accomodationTypeAdmin(admin.ModelAdmin):
	model = accomodationType
	form = accomodationTypeForm

class modeOfTransportCreationAdmin(admin.ModelAdmin):
	model = modeOfTransportCreation

class modeOfTransportAdmin(admin.ModelAdmin):
	model = modeOfTransport

class transportTypeCreationAdmin(admin.ModelAdmin):
	model = transportTypeCreation

admin.site.register(Marketing,MarketingAdmin)
admin.site.register(accomodationTypeCreation,accomodationTypeAdminCreation)
admin.site.register(accomodationStarCreation,accomodationStarAdminCreation)
admin.site.register(accomodationType,accomodationTypeAdmin)
admin.site.register(modeOfTransportCreation,modeOfTransportCreationAdmin)
admin.site.register(modeOfTransport,modeOfTransportAdmin)
admin.site.register(transportTypeCreation,transportTypeCreationAdmin)


