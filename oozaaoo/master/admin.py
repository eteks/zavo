from django.contrib import admin

from models import accomodationTypeCreation,accomodationStarCreation,accomodationType,modeOfTransportCreation,modeOfTransport,transportTypeCreation
from forms import accomodationTypeForm

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

admin.site.register(accomodationTypeCreation,accomodationTypeAdminCreation)
admin.site.register(accomodationStarCreation,accomodationStarAdminCreation)
admin.site.register(accomodationType,accomodationTypeAdmin)
admin.site.register(modeOfTransportCreation,modeOfTransportCreationAdmin)
admin.site.register(modeOfTransport,modeOfTransportAdmin)
admin.site.register(transportTypeCreation,transportTypeCreationAdmin)