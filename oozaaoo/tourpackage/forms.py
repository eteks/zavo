from __future__ import unicode_literals
from django import forms
import os
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_image(package_photos):    
	file_size = package_photos._size
	ext = os.path.splitext(package_photos.name)[1]
	valid_extensions = settings.IMAGE_TYPES
	if not ext.lower() in valid_extensions:
		raise ValidationError('Supports Only jpg/png/jpeg format.')
	if file_size > settings.MAX_UPLOAD_SIZE:
		raise ValidationError("Image file size should be less than 2 mb")

def validate_document(package_document):
	file_size = package_document._size
	ext = os.path.splitext(package_document.name)[1]
	valid_extensions = settings.DOCUMENT_TYPES
	if not ext.lower() in valid_extensions:
		raise ValidationError('Supports Only doc/docx/pdf format.')
	if file_size > settings.MAX_UPLOAD_SIZE:
		raise ValidationError("Image file size should be less than 2 mb")

class TourFileForm(forms.ModelForm):
	# package_document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	package_photos = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}),validators=[validate_image])
	package_document = forms.FileField(validators=[validate_document],required=False)