# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Booking, Coordination, Finance
# from forms import BookingForm

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
	pass
	# model = Booking
	# list_display = ('package_Name','contactAddress','contactMobile','contactMail','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','accomodationType','accomodationStar','modeOfTransport','notes','mealPlan','modePayment')
	# form = BookingForm

class CoordinationAdmin(admin.ModelAdmin):
	model = Coordination

	def get_queryset(self, request):
		qs = super(CoordinationAdmin, self).get_queryset(request)
		return qs.filter(booking_confirmation_status = 1)

class FinanceAdmin(admin.ModelAdmin):
	model = Finance

	def get_queryset(self, request):
		qs = super(FinanceAdmin, self).get_queryset(request)
		return qs.filter(coordination_confirmation_status = 1).filter(booking_confirmation_status = 1)

admin.site.register(Booking,BookingAdmin)
admin.site.register(Coordination,CoordinationAdmin)
admin.site.register(Finance,FinanceAdmin)
