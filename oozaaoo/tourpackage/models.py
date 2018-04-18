# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import TourFileForm
from django.db import models
from master.models import AbstractDefault
# from master.action import *
from django.conf import settings
# Create your models here.
def update_image(instance, filename):
	image_path = settings.IMAGES_ROOT
	image_root=image_path+"tour_"+filename
	return image_root

def update_file(instance, filename):
	file_path = settings.DOCUMENT_ROOT
	file_root=file_path+"tour_"+filename
	return file_root

class Tourpackage(AbstractDefault):
	package_name = models.CharField(verbose_name = 'Package Name', max_length = 50,help_text="Ex:Thailand",unique=True)
	package_description = models.TextField(verbose_name = 'Package Description', max_length = 1000,help_text="Details About the package")
	package_location = models.CharField(verbose_name = 'Location', max_length = 50,help_text="Add places with comma(Ex:Bangkok,Pattaya)")
	package_photos = models.ImageField(verbose_name = 'Photos to Upload',upload_to = update_image,max_length = 255,help_text="Upload Only jpg/png/jpeg format.")	
	package_document = models.FileField(verbose_name = 'Package Document',upload_to = update_file,help_text="Upload Only doc/docx/pdf format.")	
	no_of_days = models.IntegerField(verbose_name = 'No. of days',help_text="Ex:4")
	no_of_nights = models.IntegerField(verbose_name = 'No. of nights',help_text="Ex:5")
	adult_cost = models.DecimalField(verbose_name = 'Package Cost (Adult)', max_digits = 10, decimal_places = 2,help_text="Ex:10000")
	children_cost = models.DecimalField(verbose_name = 'Package Cost (Children)', max_digits = 10, decimal_places = 2,help_text="Ex:5000")
	infant_cost = models.DecimalField(verbose_name = 'Package Cost (Infant)', max_digits = 10, decimal_places = 2,help_text="Ex:2500")

	def __str__(self):
		return self.package_name

	def gal_image(self):
		files = str(self.package_photos).split(',')
		count=len(files)
		filer=''
		if count > 1:
			for x in files:
				filer = filer + '<img src="'+settings.SITE_URL+'%s" width="100px"/>' % str(x) + '&nbsp;'
			return filer
		else:
			return 'None'	
	gal_image.allow_tags = True
	gal_image.short_description = 'Image'