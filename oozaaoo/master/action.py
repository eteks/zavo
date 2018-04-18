# phone validation
from django.core.validators import RegexValidator
from django.conf import settings
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
import requests
filename_path = ""
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
	filename_path = file_root
	print "1" + filename_path
	print "2" +file_root
	return file_root
	def give_fileName():
		print "3" +filename_path
		return filename_path

def give_fileName():
	print "3" +filename_path
	return filename_path



def send_sms(mobile_number,text):
	print mobile_number
	print text
	# headers = {'Content-Type':'application/json'}
	# data = {'user':settings.SMS_USER, 'pass':settings.SMS_PASSWORD,'sender':settings.SMS_SENDER,'phone':mobile_number,'text':text,'priority':settings.SMS_PRIORITY,'stype':settings.SMS_STYPE}
	# r = requests.post('http://dnd.blackholesolution.com/api/sendmsg.php', headers=headers, params=data)

