# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Marketing

# from forms import MarketingForm,accomodationTypeForm,combinedForm
from forms import MarketingForm
from django.utils.translation import ugettext, ugettext_lazy as _

# Register your models here.
class MarketingAdmin(admin.ModelAdmin):
	model = Marketing
	# list_display = ('get_package','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','notes')
	# form = MarketingForm

	# def get_package(self, obj):
	# 	return obj.packageName
	# get_package.short_description = 'Package Name'
	# pass
	readonly_fields = ['no_of_days','total_person','created_date','modified_date']
	fieldsets = (
        (_('Customer'), {'fields': ['customer']}),
        (_('Package Wishes'), {'fields': ('places_to_visit', 'departure_date', 'arrival_date','no_of_days','no_of_nights',
        	'no_of_adult','no_of_children','no_of_infant','total_person')}),
        (_('Accomodation & Other Details'), {'fields': ('accomodation', 'mode_of_transport', 'mealplan','mealPlan_type',
        	'remarks')}),
        (_('Status and Dates'), {'fields': ('marketing_confirmation_status', 'active_status','delete_status','created_date','modified_date')}),
    )

admin.site.register(Marketing,MarketingAdmin)


