# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Marketing, Customer
import csv
from django.http import HttpResponse

# from forms import MarketingForm,accomodationTypeForm,combinedForm
from forms import MarketingForm
from django.utils.translation import ugettext, ugettext_lazy as _

def export_as_csv(modeladmin, request, queryset):
	import csv
	from django.utils.encoding import smart_str
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=marketing.csv'
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
	writer.writerow([
		# smart_str(u"ID"),
		smart_str(u"Customer Name"),
		smart_str(u"Address"),
		smart_str(u"Email"),
		smart_str(u"Mobile"),
		smart_str(u"Tour package"),
		smart_str(u"Departure"),
		smart_str(u"Arrival"),
		smart_str(u"Days"),
		smart_str(u"Nights"),
		smart_str(u"Meal Plan"),
		smart_str(u"Total Members"),
		smart_str(u"Adult"),
		smart_str(u"Children"),
		smart_str("Infants"),
		smart_str(u"Remarks"),
	])
	for obj in queryset:
		customer = Customer.objects.get(id = obj.customer_id)
		writer.writerow([
			# smart_str(obj.pk),
			smart_str(customer.customer_name),
			smart_str(customer.customer_address),
			smart_str(customer.customer_email),
			smart_str(customer.customer_mobile),
			smart_str(obj.places_to_visit),
			smart_str(obj.departure_date),
			smart_str(obj.arrival_date),
			smart_str(obj.no_of_days),
			smart_str(obj.no_of_nights),
			smart_str(obj.mealplan),
			smart_str(obj.total_person),
			smart_str(obj.no_of_adult),
			smart_str(obj.no_of_children),
			smart_str(obj.no_of_infant),
			smart_str(obj.remarks)
		])
	return response

# Register your models here.
class MarketingAdmin(admin.ModelAdmin):
	model = Marketing
	# list_display = ('get_package','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','notes')
	# form = MarketingForm
	list_display = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person',)
	list_filter = ('customer','departure_date','arrival_date','no_of_days','no_of_nights','total_person',)

	readonly_fields = ['no_of_days','total_person','created_date','modified_date','no_of_nights']
	fieldsets = (
        (_('Customer'), {'fields': ['customer']}),
        (_('Package Wishes'), {'fields': ('places_to_visit', 'departure_date', 'arrival_date','no_of_days','no_of_nights',
        	'no_of_adult','no_of_children','no_of_infant','total_person')}),
        (_('Accomodation & Other Details'), {'fields': ('accomodation', 'mode_of_transport', 'mealplan','mealPlan_type',
        	'remarks')}),
        (_('Status and Dates'), {'fields': ('marketing_confirmation_status', 'package_itinerary', 'send_mail', 'active_status','delete_status','created_date','modified_date')}),
    )
	# actions = [export_as_csv]

	def get_actions(self, request):
	    actions = super(MarketingAdmin, self).get_actions(request)
	    if 'delete_selected' in actions:
	        del actions['delete_selected']
	    return actions
	    
	# def get_actions(self, request):
	# 	actions = super(MarketingAdmin, self).get_actions(request)
	# 	return actions

admin.site.register(Marketing,MarketingAdmin)
# admin.site.add_action(export_as_csv,'export_selected_as_csv')





