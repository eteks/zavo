# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from master.models import *

# Create your models here.
class Payment(AbstractDefault):
	booking_id = models.CharField(verbose_name='Enter Booking Id',max_length=20)
	total_amount = models.DecimalField(verbose_name = 'Total Amount', max_digits = 10, decimal_places = 2) #Automatic generation
	amount_paying = models.DecimalField(verbose_name = 'Amount Paying', max_digits = 10, decimal_places = 2)
	balance_amount = models.DecimalField(verbose_name = 'Balance Amount', max_digits = 10, decimal_places = 2) #Automatic generation
	payment_mode = models.CharField(verbose_name = 'Payment Mode', max_length = 100,choices=PAYMENT_MODE) #Single selection
	remarks = models.TextField(verbose_name = "Notes, if any")

	def __str__(self):
		return self.id

	def save(self, *args, **kwargs):
		paid =  Booking.objects.filter(booking_id = self.booking_id)
		super(Marketing, self).save(*args, **kwargs)
