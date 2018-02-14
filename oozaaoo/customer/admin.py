from django.contrib import admin

from models import Customer
# Register your models here.
class customerAdmin(admin.ModelAdmin):
	model = Customer

admin.site.register(Customer,customerAdmin)
