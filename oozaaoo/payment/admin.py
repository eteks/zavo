# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Payment
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings
from forms import PaymentForm

class PaymentAdmin(admin.ModelAdmin):
	model = Payment
	form = PaymentForm
	list_display = ('booking_id','total_amount','amount_paying','balance_amount','payment_mode')
	list_filter = ('booking_id','balance_amount','created_date','active_status')
	# readonly_fields = ['total_amount','balance_amount','created_date','modified_date']
	readonly_fields = ['created_date','modified_date']
	fieldsets = (
        (_('Payment'), {'fields': ['booking_id','total_amount','amount_paying','balance_amount','payment_mode','remarks']}),
        (_('Status and Dates'), {'fields': ('active_status','delete_status','created_date','modified_date')}),
    )

	class Media:
		js = ('admin/js/jquery-1.11.3.min.js', 'admin/js/action.js')
		# js = (settings.BASE_DIR+'/admin/js/jquery-1.11.3.min.js', settings.BASE_DIR+'/admin/js/action.js')

admin.site.register(Payment,PaymentAdmin)

