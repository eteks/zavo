# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Payment

class PaymentAdmin(admin.ModelAdmin):
	model = Payment

admin.site.register(Payment,PaymentAdmin)

