from django.contrib import admin

from models import Customer
# Register your models here.
class customerAdmin(admin.ModelAdmin):
	model = Customer
	list_display = ('customer_name','customer_mobile','customer_email','customer_address')
	list_filter = ('created_date','active_status')


admin.site.register(Customer,customerAdmin)
