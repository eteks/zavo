# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
from forms import TourFileForm
import os
from django.core.files.uploadedfile import SimpleUploadedFile

# Register your models here.
def handle_uploaded_file(f):
    filename, file_ext = os.path.splitext(f.name)
    suf = SimpleUploadedFile(filename + file_ext,f.read())
    Tourpackage().package_photos.save(filename + file_ext, suf, save=False)
# Register your models here.
class TourpackageAdmin(admin.ModelAdmin):
	model = Tourpackage
	form = TourFileForm
	fields = ('active_status','delete_status','package_name','package_description','package_location','package_photos','gal_image','package_document','no_of_days','no_of_nights','adult_cost','children_cost','infant_cost','created_date','modified_date')
	readonly_fields = ['gal_image','created_date','modified_date']
	list_display = ('package_name','package_location','no_of_days','no_of_nights','adult_cost','children_cost','infant_cost')
	list_filter = ('package_name','package_location','no_of_days','no_of_nights',)
	search_fields = ('package_name','package_location','no_of_days','no_of_nights',)

	def save_model(self,request,obj,form,change,*args,**kwargs):
		counts=len(request.FILES.getlist("package_photos"))
		count=counts
		# print count
		filer=''
		files = request.FILES.getlist('package_photos')
		for x in files:
			count=count-1
			if count==0:
				filer = filer + settings.IMAGES_ROOT + 'tour_'+ str(x)
			else:
				filer = filer + settings.IMAGES_ROOT + 'tour_'+ str(x) + ','
				handle_uploaded_file(x)
		if counts!=0:
			obj.package_photos = filer
		super(Tourpackage, obj).save(*args,**kwargs)


admin.site.register(Tourpackage, TourpackageAdmin)