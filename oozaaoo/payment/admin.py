# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Payment
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings
from forms import PaymentForm

def export_as_csv(modeladmin, request, queryset):
	import csv
	from django.utils.encoding import smart_str
	from django.http import HttpResponse
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=payments.csv'
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
	writer.writerow([
		smart_str(u"Booking ID"),
		smart_str(u"Total Amount"),
		smart_str(u"Amount paid"),
		smart_str(u"Balance"),
		smart_str(u"Payment Mode"),
		smart_str(u"Remarks"),
	])
	for obj in queryset:
		writer.writerow([
			smart_str(obj.booking_id),
			smart_str(obj.total_amount),
			smart_str(obj.amount_paying),
			smart_str(obj.balance_amount),
			smart_str(obj.payment_mode),
			smart_str(obj.remarks),
		])
	return response

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
	# actions = [export_as_csv]

	def get_actions(self, request):
	    actions = super(PaymentAdmin, self).get_actions(request)
	    if 'delete_selected' in actions:
	        del actions['delete_selected']
	    return actions

	class Media:
		js = ('admin/js/jquery-1.11.3.min.js', 'admin/js/action.js')
		# js = (settings.BASE_DIR+'/admin/js/jquery-1.11.3.min.js', settings.BASE_DIR+'/admin/js/action.js')

admin.site.register(Payment,PaymentAdmin)

