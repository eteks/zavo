# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiselectfield import MultiSelectField
from django.db import models
from tourpackage.models import Tourpackage
from customer.models import Customer
from master.models import *
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.template import Context
from django.conf import settings
from master.action import send_sms

# Create your models here.
class Booking(AbstractDefault,TransportInfo):
	customer = models.ForeignKey(Customer, verbose_name = 'Customer ID')
	marketing_id = models.IntegerField(verbose_name = 'Marketing ID')
	booking_id = models.CharField(verbose_name='Auto generated booking Id',max_length=500, null = True)
	package = models.ForeignKey(Tourpackage,verbose_name = 'Package Name',max_length=50,related_name = 'package', null = True)	
	departure_date = models.DateField(verbose_name = 'Date of Departure')
	arrival_date = models.DateField(verbose_name = 'Date of Arrival')
	no_of_days = models.IntegerField(verbose_name = 'No. of days')
	no_of_nights = models.IntegerField(verbose_name = 'No. of nights')
	no_of_adult = models.IntegerField(verbose_name = 'No. of adults')
	no_of_children = models.IntegerField(verbose_name = 'No. of Children')
	no_of_infant = models.IntegerField(verbose_name = 'No. of Infant')
	total_person = models.IntegerField(verbose_name = 'Total Person')
	package_cost = models.DecimalField(verbose_name = 'Package Cost', max_digits = 10, decimal_places = 2,default = 0, help_text="Package cost will be generated automatically based on package selection" ) #Automatic generation
	discount = models.DecimalField(verbose_name = 'Discount (if any)', max_digits = 10, decimal_places = 2,default = 0) #Automatic generation
	total_cost = models.DecimalField(verbose_name = 'Total Cost', max_digits = 10, decimal_places = 2,default = 0) #Automatic generation
	paid_amount = models.DecimalField(verbose_name = 'Paid Amount', max_digits = 10, decimal_places = 2,default = 0) #Automatic generation
	accomodation = models.ManyToManyField(AccomodationStarAndType, verbose_name = 'Accomodation Type and Star')
	mode_of_transport = models.ManyToManyField(TransportModeAndType, verbose_name = 'Mode of Transport and Type')
	mealplan = MultiSelectField(verbose_name = 'Meal Plan', max_length = 100,choices=MEAL_PLAN,default = 0) #Multiple select in checkboxes
	mealPlan_type = MultiSelectField(verbose_name = 'Meal Plan Type', max_length = 100,choices=MEAL_PLAN_TYPE,default = 0) #Multiple select in checkboxes
	remarks = models.TextField(verbose_name = "Notes, if any")
	booking_confirmation_status = models.BooleanField(verbose_name ='Booking Team Confirmation status', default = False)
	coordination_confirmation_status = models.BooleanField(verbose_name ='Co-ordination Team Confirmation status', default = False)
	finance_confirmation_status = models.BooleanField(verbose_name ='Finance Team Confirmation status', default = False)
	customer_status = models.TextField(verbose_name = 'Customer status', max_length = 65000)

	def clean(self):
		days_diff = self.arrival_date - self.departure_date
		diff = int(days_diff.days)
		# Don't allow draft entries to have a pub_date.
		if diff < 0:
			raise ValidationError("Arrival date should be higher than departure date")

	def save(self, *args, **kw):
		# Saving the no. of days automatically from departure_date and arrival_date
		days_diff = self.arrival_date - self.departure_date
		diff = int(days_diff.days)
		self.no_of_days = diff
		# Saving the no. of person automatically by counting adult, children and infant
		self.total_person = int(self.no_of_adult + self.no_of_children + self.no_of_infant)
		# Saving the total cost from package cost and discount
		self.total_cost = self.package_cost - self.discount
		if self.pk:
			old_object = Booking.objects.get(id=self.pk)
			if self.booking_confirmation_status and old_object.booking_confirmation_status==0:
				status='Oozaaoo Booking Status'
				message='Your booking process was completed our coordination team will contact you regarding the ticket conformation with the schedule plan.'
				# print "update_form"
				# send_mail('Test', 'Hi buddy', 'kalaimca.gs@gmail.com', ['anand@etekchnoservices.com'])
				# if self.pk is not None and self.coordination_confirmation_status:
				# 	status='Oozaaoo Tour Plan Status'
				# 	message='Your tour plan was scheduled and the information was attached with this mail. Please contact us if you have any queries.'
				# plaintext = get_template('email.txt')
				# if self.pk is not None and self.finance_confirmation_status:
				# 	status='Oozaaoo Finance Status'
				# 	message='Your booking process was completed our coordination team will contact you regarding the ticket conformation with the schedule plan.'
				# d = Context({ 'username': self.customer.customer_name,'message':message })
				# htmly=render_to_string('email.html',d)
				# subject, from_email, to = status, settings.EMAIL_HOST_USER, self.customer.customer_email
				# text_content = status
				# html_content = htmly
				# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
				# msg.attach_alternative(html_content, "text/html")
				# msg.send()
				# send_sms(self.customer.customer_mobile,message_text)

		if self.pk is None and self.booking_confirmation_status:
			status='Oozaaoo Booking Status'
			message='Your booking process was completed our coordination team will contact you regarding the ticket conformation with the schedule plan.'
			# print "update_form"
			# send_mail('Test', 'Hi buddy', 'kalaimca.gs@gmail.com', ['anand@etekchnoservices.com'])
			# if self.pk is not None and self.coordination_confirmation_status:
			# 	status='Oozaaoo Tour Plan Status'
			# 	message='Your tour plan was scheduled and the information was attached with this mail. Please contact us if you have any queries.'
			# plaintext = get_template('email.txt')
				# if self.pk is not None and self.finance_confirmation_status:
				# 	status='Oozaaoo Finance Status'
				# 	message='Your booking process was completed our coordination team will contact you regarding the ticket conformation with the schedule plan.'
			# d = Context({ 'username': self.customer.customer_name,'message':message })
			# htmly=render_to_string('email.html',d)
			# subject, from_email, to = status, settings.EMAIL_HOST_USER, self.customer.customer_email
			# text_content = status
			# html_content = htmly
			# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			# msg.attach_alternative(html_content, "text/html")
			# msg.send()

			# SMS CODE
			# send_sms(self.customer.customer_mobile,message_text)		

		super( Booking, self ).save( *args, **kw )	

	def __str__(self):
		return self.customer.customer_name

class Coordination(Booking):

	def save(self, *args, **kw):
		if self.pk:
			old_object = Coordination.objects.get(id=self.pk)
			if self.coordination_confirmation_status and old_object.coordination_confirmation_status==0:
				status='Oozaaoo Tour Plan Status'
				message='Your tour plan was scheduled and the information was attached with this mail. Please contact us if you have any queries.'
				# d = Context({ 'username': self.customer.customer_name,'message':message })
				# htmly=render_to_string('email.html',d)
				# subject, from_email, to = status, settings.EMAIL_HOST_USER, 'anand@etekchnoservices.com'
				# text_content = status
				# html_content = htmly
				# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
				# msg.attach_alternative(html_content, "text/html")
				# msg.send()
				# SMS CODE
				# send_sms(self.customer.customer_mobile,message_text)

		if self.pk is None and self.coordination_confirmation_status:
			status='Oozaaoo Tour Plan Status'
			message='Your tour plan was scheduled and the information was attached with this mail. Please contact us if you have any queries.'
			# d = Context({ 'username': self.customer.customer_name,'message':message })
			# htmly=render_to_string('email.html',d)
			# subject, from_email, to = status, settings.EMAIL_HOST_USER, self.customer.customer_email
			# text_content = status
			# html_content = htmly
			# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			# msg.attach_alternative(html_content, "text/html")
			# msg.send()
			# SMS CODE
			# send_sms(self.customer.customer_mobile,message_text)	
		super( Coordination, self ).save( *args, **kw )
	class Meta:
		proxy = True

class Finance(Coordination):
    class Meta:
        proxy = True