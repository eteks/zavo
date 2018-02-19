# phone validation
from django.core.validators import RegexValidator
from django.conf import settings
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# date validation
# def validate_date(value):
# 	v1 = value
# 	print v1
	
def update_image(instance, filename):
	image_path = settings.IMAGES_ROOT
	image_root=image_path+"tour_"+filename
	return image_root

def update_file(instance, filename):
	file_path = settings.DOCUMENT_ROOT
	file_root=file_path+"tour_"+filename
	return file_root
