from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
	customer_name = models.CharField(verbose_name = 'Customer Name', max_length = 50)
	customer_mobile = models.BigIntegerField(verbose_name = 'Customer Contact No.')
	customer_email = models.EmailField(verbose_name = 'Customer Email ID', max_length = 50)
	customer_address = models.TextField(verbose_name = 'Customer Address', max_length = 1000)
	customer_alt_mobile = models.BigIntegerField(verbose_name = 'Customer Alternate Contact No.')

	def __str__(self):
		return self.customer_name


