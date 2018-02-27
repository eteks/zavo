from __future__ import unicode_literals

from django.db import models
from master.models import AbstractDefault
from oozaaoo.action import *
from django.core.validators import RegexValidator
# Create your models here.
class Customer(AbstractDefault):
	
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	customer_name = models.CharField(verbose_name = 'Customer Name', max_length = 50,help_text="Ex:Claris")
	customer_mobile = models.BigIntegerField(validators=[phone_regex],verbose_name = 'Customer Contact No.',unique=True,help_text="Ex:9944919023")
	customer_alt_mobile = models.BigIntegerField(verbose_name = 'Customer Alternate Contact No.',blank=True, null=True)
	customer_email = models.EmailField(verbose_name = 'Customer Email ID', max_length = 50,unique=True,help_text="Ex:test@gmail.com")
	customer_address = models.TextField(verbose_name = 'Customer Address', max_length = 1000)
	
	def __str__(self):
		return self.customer_name