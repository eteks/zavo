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

def export_as_csv(modeladmin, request, queryset):
	import csv
	from django.utils.encoding import smart_str
	from django.http import HttpResponse
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=tour_packages.csv'
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
	writer.writerow([
		smart_str(u"Package Name"),
		smart_str(u"Description"),
		smart_str(u"Location"),
		smart_str(u"Days"),
		smart_str(u"Nights"),
		smart_str(u"Cost (Adult)"),
		smart_str(u"Cost (Children)"),
		smart_str(u"Cost (Infant)"),
	])
	for obj in queryset:
		writer.writerow([
			smart_str(obj.package_name),
			smart_str(obj.package_description),
			smart_str(obj.package_location),
			smart_str(obj.no_of_days),
			smart_str(obj.no_of_nights),
			smart_str(obj.adult_cost),
			smart_str(obj.children_cost),
			smart_str(obj.infant_cost),
		])
	return response

# Register your models here.
class TourpackageAdmin(admin.ModelAdmin):
	model = Tourpackage
	form = TourFileForm
	fields = ('active_status','delete_status','package_name','package_description','package_location','package_photos','gal_image','package_document','no_of_days','no_of_nights','adult_cost','children_cost','infant_cost')
	readonly_fields = ['gal_image','created_date','modified_date']
	list_display = ('package_name','package_location','no_of_days','no_of_nights','adult_cost','children_cost','infant_cost')
	list_filter = ('package_name','package_location','no_of_days','no_of_nights','created_date','active_status')
	# actions = [export_as_csv]

	def get_actions(self, request):
	    actions = super(TourpackageAdmin, self).get_actions(request)
	    if 'delete_selected' in actions:
	        del actions['delete_selected']
	    return actions

	
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