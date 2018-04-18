# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.functional import lazy
from django.db import models
from customer.models import Customer
from master.models import *
from booking.models import Booking
from multiselectfield import MultiSelectField
import datetime
from django.db.models.signals import post_save
from django.core.mail import send_mail
from master.action import *
import requests
import os
from django.core.mail import EmailMessage
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.core.exceptions import ValidationError
from master.action import send_sms
import socket
socket.getaddrinfo('localhost', 8080)
# ACCOMODATION_TYPE = (
# 		('1', 'Hotel'),
# 		('2', 'Resort')
# 	)
# ACCOMODATION_STAR =	(
# 		('1','2 Star'),
# 		('2','3 Star'),
# 		('3','4 Star'),
# 		('4','5 Star')
# 	)
# MODEOFTRANSPORT = (
#     	('1','FLIGHT'),
#     	('2','TRAIN'),
#     	('3','BUS'),
#     	('4','CAR'),
#     	('5','GROUP')
# 	)
# FLIGHT = (
# 		('1','ECONOMY'),
# 	    ('2','BUSINESS CLASS')
# 	)
# TRAIN = (
# 		('1','AC'),
# 	 	('2','NON AC')
# 	)
# BUS = (
# 		('1','SLEEPER'),
# 		('2','SEMI-SLEEPER')
# 	)
# CAR = (
# 		('1','INDIGO'),
# 		('2','INNOVA'),
# 		('3','TEMPO')
# 	)
# GROUP = (
# 		 ('1','MINI BUS'),
# 		 ('2','BUS')
# 	)

# @receiver(post_save,sender = Marketing)

class Marketing(AbstractDefault):
	customer = models.ForeignKey(Customer, verbose_name = 'Customer ID')
	places_to_visit = models.CharField(verbose_name = 'Places to Visit',max_length=255)
	departure_date = models.DateField(verbose_name = 'Date of Departure')
	arrival_date = models.DateField(verbose_name = 'Date of Arrival')
	no_of_days = models.IntegerField(verbose_name = 'No. of days',help_text="Auto generated by system based on departure and arrival date",null=True)
	no_of_nights = models.IntegerField(verbose_name = 'No. of nights',help_text="Auto generated by system based on departure and arrival date",null=True)
	no_of_adult = models.IntegerField(verbose_name = 'No. of adults')
	no_of_children = models.IntegerField(verbose_name = 'No. of Children')
	no_of_infant = models.IntegerField(verbose_name = 'No. of Infant')
	total_person = models.IntegerField(verbose_name = 'Total Person',help_text="Auto generated by system based on counting the no. of adult, children and infant",null=True)	
	accomodation = models.ManyToManyField(AccomodationStarAndType, verbose_name = 'Accomodation Type')
	mode_of_transport = models.ManyToManyField(TransportModeAndType, verbose_name = 'Mode of Transport')
	mealplan = MultiSelectField(verbose_name = 'Meal Plan', max_length = 100,choices=MEAL_PLAN) #Multiple select in checkboxes
	mealPlan_type = MultiSelectField(verbose_name = 'Meal Plan Type', max_length = 100,choices=MEAL_PLAN_TYPE) #Multiple select in checkboxes
	remarks = models.TextField(verbose_name = "Notes, if any")
	marketing_confirmation_status = models.BooleanField(verbose_name ='Marketing Team Confirmation status', default = False)
	package_itinerary = models.FileField(verbose_name = 'Package itinerary',upload_to = update_file, default = '')	
	send_mail = models.BooleanField(verbose_name = 'Send E-mail', default = False)

	def __str__(self):
		# print os.path.basename(self.package_itinerary.name)
		return unicode(self.id)

	def filename(self):
		print os.path.basename(self.package_itinerary.name)
		return os.path.basename(self.package_itinerary.name)
		
	def clean(self):
		days_diff = self.arrival_date - self.departure_date
		diff = int(days_diff.days)
		# Don't allow draft entries to have a pub_date.
		if diff < 0:
			raise ValidationError("Arrival date should be higher than departure date")

	def save(self, *args, **kwargs):
		# Saving the no. of days automatically from departure_date and arrival_date
		days_diff = self.arrival_date - self.departure_date
		diff = int(days_diff.days)
		self.no_of_days = diff
		self.no_of_nights = diff-1;
		# Saving the no. of person automatically by counting adult, children and infant
		self.total_person = int(self.no_of_adult + self.no_of_children + self.no_of_infant)
		# if self.pk is not None and self.marketing_confirmation_status and self.send_mail:
		# if self.marketing_confirmation_status and self.send_mail:
		# 	# print "update_form"
		# 	# send_mail('Test', 'Hi buddy', 'kalaimca.gs@gmail.com', ['anand@etekchnoservices.com'])
		# 	# plaintext = get_template('email.txt')
		# 	# htmly=get_template('emaself.pk is not None and il.html')

		# 	# d = Context({ 'username': self.customer.customer_name })	
		# 	# subject, from_email, to = 'Oozaaoo Marketing Status', settings.EMAIL_HOST_USER, 'harihara@etekchnoservices.com'
		# 	# text_content = "Oozaaoo Marketing Status"
		# 	# html_content = htmly.render(d)
		# 	# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		# 	# msg.attach_alternative(html_content, "text/html")
		# 	# msg.send()
		# 	message = EmailMessage(
		# 	    'Hello', # Subject
		# 	    'Here is the message.', # Message
		# 	    'harihara@etekchnoservices.com', #From
		# 	    ['harihara@etekchnoservices.com'], #To
		# 	    ['hariharaprabu@ymail.com'], #BCC
		# 	    reply_to=['harihara@etekchnoservices.com'],
		# 	    headers={'Message-ID': 'foo'},
		# 	)
		# 	file_root = give_fileName()
		# 	print "4" + file_root
		# 	# message.attach(file_root)
		# 	message.send()
			# send_mail(
			#     'Oozaaoo Marketing Status', # Subject
			#     'Here is the message.', # Message
			#     'harihara@etekchnoservices.com', #From 
			#     ['harihara@etekchnoservices.com'], #To
			#     fail_silently=False,
			# )
			# subject, from_email, to = 'hello', 'kalaimca.gs@gmail.com', 'anand@etekchnoservices.com'
			# text_content = 'This is an important message.'
			# html_content = '<p>This is an <strong>important</strong> message.</p>'
			# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			# msg.attach_alternative(html_content, "text/html")
			# msg.send()

		message_text = "marketing_confirmation_status"
		if self.pk:
			old_object = Marketing.objects.get(id=self.pk)
			if self.marketing_confirmation_status and old_object.marketing_confirmation_status==0:
				# print "sending_sms_and_email_edit"
				# SMS CODE
				send_sms(self.customer.customer_mobile,message_text)

		if self.pk is None and self.marketing_confirmation_status:
			# print "update_form"
			# send_mail('Test', 'Hi buddy', 'kalaimca.gs@gmail.com', ['anand@etekchnoservices.com'])
			# plaintext = get_template('email.txt')
			#comment started
			# htmly=get_template('email.html')

			# d = Context({ 'username': self.customer.customer_name })	
			# subject, from_email, to = 'Oozaaoo Marketing Status', settings.EMAIL_HOST_USER, self.customer.customer_email
			# text_content = "Oozaaoo Marketing Status"
			# html_content = htmly.render(d)
			# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			# msg.attach_alternative(html_content, "text/html")
			# msg.send()
			#comment end
			# subject, from_email, to = 'hello', 'kalaimca.gs@gmail.com', 'anand@etekchnoservices.com'
			# text_content = 'This is an important message.'
			# html_content = '<p>This is an <strong>important</strong> message.</p>'
			# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			# msg.attach_alternative(html_content, "text/html")
			# msg.send()

			# SMS CODE
			send_sms(self.customer.customer_mobile,message_text)

			
		# print self.accomodation
		if(self.marketing_confirmation_status):
			b = Booking.objects.filter(created_date__startswith = datetime.date.today()).count()
			count = Marketing.objects.all().count()
			if(self.created_date.month >= 10):
				month = str(self.created_date.month)
			else:
				month = '0' + str(self.created_date.month)
			if(self.created_date.day >= 10):
				day = str(self.created_date.day)
			else:
				day = '0' + str(self.created_date.day)
			# # accomodation = AccomodationStarAndType.objects.create(accomodation_type = '2 star', accomodation_star = 'Hotel')
			# print self.accomodation
			if self.pk is not None:
				Booking.objects.filter(marketing_id = self.pk).update(customer = self.customer, remarks = self.remarks, departure_date = self.departure_date, arrival_date = self.arrival_date, no_of_days = self.no_of_days, 
					no_of_nights = self.no_of_nights, no_of_adult = self.no_of_adult, no_of_infant = self.no_of_infant, no_of_children = self.no_of_children, total_person = self.total_person, mealplan = self.mealplan, mealPlan_type = self.mealPlan_type)
			else:
				book = Booking(marketing_id = count + 1, customer = self.customer, remarks = self.remarks, departure_date = self.departure_date, arrival_date = self.arrival_date, no_of_days = self.no_of_days, 
					no_of_nights = self.no_of_nights, no_of_adult = self.no_of_adult, no_of_infant = self.no_of_infant, no_of_children = self.no_of_children, total_person = self.total_person,mealplan = self.mealplan, mealPlan_type = self.mealPlan_type,
					booking_id = 'BOOKID' + '_' + unicode(day +  month + str(self.created_date.year)) + '_' + str(b+1))
				book.save()
				# mobile = Customer.objects.filter(id = self.customer_id).values('customer_mobile').get()
				# print mobile
				# headers = {'Content-Type':'application/json'}
				# data = {'user':'VALLIK', 'pass':'abcd1234','sender':'VALLIK','phone':'9790022747','text':'Your requirements received! Our booking team will contact you soon.','priority':'ndnd','stype':'normal'}
				# r = requests.post('http://dnd.blackholesolution.com/api/sendmsg.php', headers=headers, params=data)
		# if self.marketing_confirmation_status and self.send_mail:
		# 	# print "update_form"
		# 	# send_mail('Test', 'Hi buddy', 'kalaimca.gs@gmail.com', ['anand@etekchnoservices.com'])
		# 	# plaintext = get_template('email.txt')
		# 	# htmly=get_template('emaself.pk is not None and il.html')

		# 	# d = Context({ 'username': self.customer.customer_name })	
		# 	# subject, from_email, to = 'Oozaaoo Marketing Status', settings.EMAIL_HOST_USER, 'harihara@etekchnoservices.com'
		# 	# text_content = "Oozaaoo Marketing Status"
		# 	# html_content = htmly.render(d)
		# 	# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		# 	# msg.attach_alternative(html_content, "text/html")
		# 	# msg.send()
		# 	print "1"
		# 	message = EmailMessage(
		# 	    'Hello', # Subject
		# 	    'Here is the message.', # Message
		# 	    'harihara@etekchnoservices.com', #From
		# 	    ['harihara@etekchnoservices.com'], #To
		# 	    ['hariharaprabu@ymail.com'], #BCC
		# 	    reply_to=['harihara@etekchnoservices.com'],
		# 	    headers={'Message-ID': 'foo'},
		# 	)
		# 	file_root = give_fileName()
		# 	print "4" + file_root
		# 	message.attach(file_root)
		# 	message.send()

		super(Marketing, self).save(*args, **kwargs)

def post(sender, instance,created, **kwargs):
	# print Marketing.package_itinerary
	# if instance.marketing_confirmation_status and instance.send_mail:
	# 	# print "update_form"
	# 	# send_mail('Test', 'Hi buddy', 'kalaimca.gs@gmail.com', ['anand@etekchnoservices.com'])
	# 	# plaintext = get_template('email.txt')
	# 	# htmly=get_template('emaself.pk is not None and il.html')
	# 	# d = Context({ 'username': self.customer.customer_name })	
	# 	# subject, from_email, to = 'Oozaaoo Marketing Status', settings.EMAIL_HOST_USER, 'harihara@etekchnoservices.com'
	# 	# text_content = "Oozaaoo Marketing Status"
	# 	# html_content = htmly.render(d)
	# 	# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	# 	# msg.attach_alternative(html_content, "text/html")
	# 	# msg.send()
	# print instance.package_itinerary
	customer = Customer.objects.filter(id = instance.customer_id)
	for obj in customer:
		to_email = obj.customer_email
		name = obj.customer_name
	message = EmailMessage(
	    'Oozaaoo - Package Enquiry', # Subject
	    'Hi '+ name + ', \nThanks for contacting us. \nWe have attached an package itinerary with regard to your queries. Our marketing team will contact you soon for further process. \n\nThanks & Regards, \n Marketing team - Oozaaoo', # Message
	    'admin@oozaoo.com', #From
	    [to_email], #To
	    ['admin@oozaoo.com'], #BCC
	    reply_to=['admin@oozaaoo.com'],
	    headers={'Message-ID': 'foo'},
	)
	print instance.package_itinerary
	message.attach(instance.package_itinerary.name,instance.package_itinerary.read())
	# message.attach_file('/media/document/tour_Mahindra Global IVN Architecture Design_Business_Requirements.doc')
	message.send()
post_save.connect(post, sender=Marketing)



