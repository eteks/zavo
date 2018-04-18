# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Booking, Coordination, Finance, Customer, Tourpackage
# from forms import BookingForm
from django.utils.translation import ugettext, ugettext_lazy as _

def export_as_csv(modeladmin, request, queryset):
	import csv
	from django.utils.encoding import smart_str
	from django.http import HttpResponse
	response = HttpResponse(content_type='text/csv')
	if modeladmin.value == 'booking':
		response['Content-Disposition'] = 'attachment; filename=booking.csv'
	elif modeladmin.value == 'coordination':
		response['Content-Disposition'] = 'attachment; filename=coordination.csv'
	elif modeladmin.value == 'finance':
		response['Content-Disposition'] = 'attachment; filename=finance.csv'
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
	writer.writerow([
		# smart_str(u"ID"),
		smart_str(u"Booking ID"),
		smart_str(u"Customer Name"),
		smart_str(u"Address"),
		smart_str(u"Email"),
		smart_str(u"Mobile"),
		smart_str(u"Package Name"),
		smart_str(u"Departure"),
		smart_str(u"Arrival"),
		smart_str(u"Days"),
		smart_str(u"Nights"),
		smart_str(u"Meal Plan"),
		smart_str(u"Total Members"),
		smart_str(u"Adult"),
		smart_str(u"Children"),
		smart_str("Infants"),
		smart_str("Package Cost"),
		smart_str("Discount"),
		smart_str("Total Cost"),
		smart_str("Paid Amount"),
		smart_str("Booking Status"),
		smart_str("Coordination Status"),
		smart_str("Finance Status"),
		smart_str("Customer Status"),
		smart_str(u"Remarks"),
	])
	for obj in queryset:
		customer = Customer.objects.get(id = obj.customer_id)
		if obj.package_id:
			package = Tourpackage.objects.get(id = obj.package_id)
			packageName = package.package_name
		else:
			packageName = ""

		writer.writerow([
			# smart_str(obj.pk),
			smart_str(obj.booking_id),
			smart_str(customer.customer_name),
			smart_str(customer.customer_address),
			smart_str(customer.customer_email),
			smart_str(customer.customer_mobile),
			smart_str(packageName),
			smart_str(obj.departure_date),
			smart_str(obj.arrival_date),
			smart_str(obj.no_of_days),
			smart_str(obj.no_of_nights),
			smart_str(obj.mealplan),
			smart_str(obj.total_person),
			smart_str(obj.no_of_adult),
			smart_str(obj.no_of_children),
			smart_str(obj.no_of_infant),
			smart_str(obj.package_cost),
			smart_str(obj.discount),
			smart_str(obj.total_cost),
			smart_str(obj.paid_amount),
			smart_str(obj.booking_confirmation_status),
			smart_str(obj.coordination_confirmation_status),
			smart_str(obj.finance_confirmation_status),
			smart_str(obj.customer_status),
			smart_str(obj.remarks)
		])
	return response

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
	value = 'booking'
	model = Booking

	list_display = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status')
	list_filter = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status','created_date','active_status')
	
	readonly_fields = ['booking_id','no_of_days','total_person','created_date','modified_date','paid_amount','total_cost','finance_confirmation_status','coordination_confirmation_status']
	fieldsets = (
        (_('Customer Details'), {'fields': ['customer','booking_id']}),
        (_('Packages'), {'fields': ('package', 'departure_date', 'arrival_date','no_of_days','no_of_nights',
        	'no_of_adult','no_of_children','no_of_infant','total_person')}),
        (_('Cost Details'), {'fields': ('package_cost', 'discount', 'total_cost','paid_amount')}),
        (_('Transport Details'), {'fields': ('mode_of_transport','transport_name','departure_time','arrival_time','remarks')}),
        (_('Accomodation Details'),{'fields':('accomodation','mealplan','mealPlan_type','hotel_name','room_no','check_in','check_out')}),
        (_('Status and Dates'), {'fields': ('booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status', 'active_status','delete_status','created_date','modified_date')}),
    )
	# actions = [export_as_csv]
	
	def get_actions(self, request):
	    actions = super(BookingAdmin, self).get_actions(request)
	    if 'delete_selected' in actions:
	        del actions['delete_selected']
	    return actions

	def has_add_permission(self, request):
		return False

	# def get_actions(self, request):
	# 	actions = super(BookingAdmin, self).get_actions(request)
	# 	return actions

class CoordinationAdmin(admin.ModelAdmin):
	value = 'coordination'
	model = Coordination
	list_display = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status')
	list_filter = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status','created_date','active_status')
	readonly_fields = ['booking_id','no_of_days','total_person','created_date','modified_date','paid_amount','total_cost','booking_confirmation_status','finance_confirmation_status']
	fieldsets = (
        (_('Customer Details'), {'fields': ['customer','booking_id']}),
        (_('Packages'), {'fields': ('package', 'departure_date', 'arrival_date','no_of_days','no_of_nights',
        	'no_of_adult','no_of_children','no_of_infant','total_person')}),
        (_('Cost Details'), {'fields': ('package_cost', 'discount', 'total_cost','paid_amount')}),
        (_('Transport Details'), {'fields': ('mode_of_transport','transport_name','departure_time','arrival_time','remarks')}),
        (_('Accomodation Details'),{'fields':('accomodation','mealplan','mealPlan_type','hotel_name','room_no','check_in','check_out')}),
        (_('Status and Dates'), {'fields': ('booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status','customer_status', 'active_status','delete_status','created_date','modified_date')}),
    )
	# actions = [export_as_csv]

	def get_actions(self, request):
	    actions = super(CoordinationAdmin, self).get_actions(request)
	    if 'delete_selected' in actions:
	        del actions['delete_selected']
	    return actions

	def has_add_permission(self, request):
		return False

	# def get_queryset(self, request):
	# 	qs = super(CoordinationAdmin, self).get_queryset(request)
	# 	return qs.filter(booking_confirmation_status = 1)

class FinanceAdmin(admin.ModelAdmin):
	value = 'finance'
	model = Finance
	list_display = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status')
	list_filter = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person','booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status','created_date','active_status')
	readonly_fields = ['booking_id','no_of_days','total_person','created_date','modified_date','paid_amount','total_cost','coordination_confirmation_status','booking_confirmation_status','customer_status']
	fieldsets = (
        (_('Customer Details'), {'fields': ['customer','booking_id']}),
        (_('Packages'), {'fields': ('package', 'departure_date', 'arrival_date','no_of_days','no_of_nights',
        	'no_of_adult','no_of_children','no_of_infant','total_person')}),
        (_('Cost Details'), {'fields': ('package_cost', 'discount', 'total_cost','paid_amount')}),
        (_('Transport Details'), {'fields': ('mode_of_transport','transport_name','departure_time','arrival_time','remarks')}),
        (_('Accomodation Details'),{'fields':('accomodation','mealplan','mealPlan_type','hotel_name','room_no','check_in','check_out')}),
        (_('Status and Dates'), {'fields': ('booking_confirmation_status','coordination_confirmation_status','finance_confirmation_status', 'active_status','delete_status','created_date','modified_date')}),
    )
	# actions = [export_as_csv]

	def get_actions(self, request):
	    actions = super(FinanceAdmin, self).get_actions(request)
	    if 'delete_selected' in actions:
	        del actions['delete_selected']
	    return actions

	def has_add_permission(self, request):
		return False

	# def get_queryset(self, request):
	# 	qs = super(FinanceAdmin, self).get_queryset(request)
	# 	return qs.filter(coordination_confirmation_status = 1).filter(booking_confirmation_status = 1)

admin.site.register(Booking,BookingAdmin)
admin.site.register(Coordination,CoordinationAdmin)
admin.site.register(Finance,FinanceAdmin)
