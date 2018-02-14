from django.contrib import admin

from models import *
from forms import *

# class accomodationTypeAdminCreation(admin.ModelAdmin):
# 	model = accomodationTypeCreation

# class accomodationStarAdminCreation(admin.ModelAdmin):
# 	model = accomodationStarCreation

# class accomodationTypeAdmin(admin.ModelAdmin):
# 	model = accomodationType
# 	form = accomodationTypeForm

# class modeOfTransportCreationAdmin(admin.ModelAdmin):
# 	model = modeOfTransportCreation

# class modeOfTransportAdmin(admin.ModelAdmin):
# 	model = modeOfTransport

# class transportTypeCreationAdmin(admin.ModelAdmin):
# 	model = transportTypeCreation

# admin.site.register(accomodationTypeCreation,accomodationTypeAdminCreation)
# admin.site.register(accomodationStarCreation,accomodationStarAdminCreation)
# admin.site.register(accomodationType,accomodationTypeAdmin)
# admin.site.register(modeOfTransportCreation,modeOfTransportCreationAdmin)
# admin.site.register(modeOfTransport,modeOfTransportAdmin)
# admin.site.register(transportTypeCreation,transportTypeCreationAdmin)

class AccomodationTypeAdmin(admin.ModelAdmin):
	pass

class AccomodationStarAdmin(admin.ModelAdmin):
	pass

class ModeOfTransportAdmin(admin.ModelAdmin):
	pass

class TransportTypeAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(AccomodationType,AccomodationTypeAdmin)
admin.site.register(AccomodationStar,AccomodationStarAdmin)
admin.site.register(ModeOfTransport,ModeOfTransportAdmin)
admin.site.register(TransportType,TransportTypeAdmin)