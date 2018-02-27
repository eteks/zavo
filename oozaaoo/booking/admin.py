# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Booking, Coordination, Finance
# from forms import BookingForm
from django.utils.translation import ugettext, ugettext_lazy as _
from booking.forms import *


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
	model = Booking
	form = BookingForm

	# list_display = ('get_package','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','notes')
	# form = MarketingForm

	# def get_package(self, obj):
	# 	return obj.packageName
	# get_package.short_description = 'Package Name'
	# pass
	list_display = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status')
	list_filter = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status')
	search_fields = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person',)
	# readonly_fields = ['no_of_days','total_person','created_date','modified_date','paid_amount','total_cost']
	readonly_fields = ['booking_id','created_date','modified_date','finance_confirmation_status','coordination_confirmation_status']
	fieldsets = (
        (_('Customer Details'), {'fields': ['customer','booking_id']}),
        (_('Packages'), {'fields': ('package', 'departure_date', 'arrival_date','no_of_days','no_of_nights',
        	'no_of_adult','no_of_children','no_of_infant','total_person')}),
        (_('Cost Details'), {'fields': ('package_cost', 'discount', 'total_cost','paid_amount')}),
        (_('Accomodation & Other Details'), {'fields': ('accomodation', 'mode_of_transport', 'mealplan','mealPlan_type',
        	'remarks')}),
        (_('Status and Dates'), {'fields': ('booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status', 'active_status','delete_status','created_date','modified_date')}),
    )

	# model = Booking
	# list_display = ('package_Name','contactAddress','contactMobile','contactMail','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','accomodationType','accomodationStar','modeOfTransport','notes','mealPlan','modePayment')
	# form = BookingForm
	def has_add_permission(self, request):
		return False

	class Media:
		js = ('admin/js/jquery-1.11.3.min.js', 'admin/js/action.js')

class CoordinationAdmin(admin.ModelAdmin):
	model = Coordination
	list_display = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status')
	list_filter = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status','created_date','active_status')
	readonly_fields = ['booking_id','no_of_days','total_person','created_date','modified_date','paid_amount','total_cost','booking_confirmation_status','finance_confirmation_status']
	fieldsets = (
        (_('Customer Details'), {'fields': ['customer','booking_id']}),
        (_('Packages'), {'fields': ('package', 'departure_date', 'arrival_date','no_of_days','no_of_nights',
        	'no_of_adult','no_of_children','no_of_infant','total_person')}),
        (_('Cost Details'), {'fields': ('package_cost', 'discount', 'total_cost','paid_amount')}),
        (_('Accomodation & Other Details'), {'fields': ('accomodation', 'mode_of_transport', 'mealplan','mealPlan_type',
        	'remarks')}),
        (_('Status and Dates'), {'fields': ('booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status', 'active_status','delete_status','created_date','modified_date')}),
    )

	def has_add_permission(self, request):
		return False

	def get_queryset(self, request):
		qs = super(CoordinationAdmin, self).get_queryset(request)
		return qs.filter(booking_confirmation_status = 1)

class FinanceAdmin(admin.ModelAdmin):
	model = Finance
	list_display = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status')
	list_filter = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status','created_date','active_status')
	readonly_fields = ['booking_id','no_of_days','total_person','created_date','modified_date','paid_amount','total_cost','coordination_confirmation_status','booking_confirmation_status']
	fieldsets = (
        (_('Customer Details'), {'fields': ['customer','booking_id']}),
        (_('Packages'), {'fields': ('package', 'departure_date', 'arrival_date','no_of_days','no_of_nights',
        	'no_of_adult','no_of_children','no_of_infant','total_person')}),
        (_('Cost Details'), {'fields': ('package_cost', 'discount', 'total_cost','paid_amount')}),
        (_('Accomodation & Other Details'), {'fields': ('accomodation', 'mode_of_transport', 'mealplan','mealPlan_type',
        	'remarks')}),
        (_('Status and Dates'), {'fields': ('booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status', 'active_status','delete_status','created_date','modified_date')}),
    )

	def has_add_permission(self, request):
		return False

	def get_queryset(self, request):
		qs = super(FinanceAdmin, self).get_queryset(request)
		return qs.filter(coordination_confirmation_status = 1).filter(booking_confirmation_status = 1)

admin.site.register(Booking,BookingAdmin)
admin.site.register(Coordination,CoordinationAdmin)
admin.site.register(Finance,FinanceAdmin)
