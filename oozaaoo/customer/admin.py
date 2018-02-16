from django.contrib import admin

from models import Customer
# Register your models here.
class customerAdmin(admin.ModelAdmin):
	model = Customer
	list_display = ('customer_name','customer_mobile','customer_email')
	list_filter = ('customer_name','customer_mobile','customer_email',)
	search_fields = ('customer_name','customer_mobile','customer_email',)

admin.site.register(Customer,customerAdmin)
