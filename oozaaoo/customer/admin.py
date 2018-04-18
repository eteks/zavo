from django.contrib import admin

from models import Customer
# Register your models here.

def export_as_csv(modeladmin, request, queryset):
	import csv
	from django.utils.encoding import smart_str
	from django.http import HttpResponse
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=customer.csv'
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
	writer.writerow([
		smart_str(u"Customer Name"),
		smart_str(u"Address"),
		smart_str(u"Email"),
		smart_str(u"Mobile"),
		smart_str(u"Alternate Mobile Number"),
	])
	for obj in queryset:
		writer.writerow([
			smart_str(obj.customer_name),
			smart_str(obj.customer_address),
			smart_str(obj.customer_email),
			smart_str(obj.customer_mobile),
			smart_str(obj.customer_alt_mobile),
		])
	return response

class customerAdmin(admin.ModelAdmin):
	model = Customer
	list_display = ('customer_name','customer_mobile','customer_email','customer_address')
	list_filter = ('created_date','active_status')
	readonly_fields = ['created_date','modified_date']
	# actions = [export_as_csv]

	def get_actions(self, request):
	    actions = super(customerAdmin, self).get_actions(request)
	    if 'delete_selected' in actions:
	        del actions['delete_selected']
	    return actions

admin.site.register(Customer,customerAdmin)
