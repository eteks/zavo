# phone validation
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
import requests
# date validation
# def validate_date(value):
# 	v1 = value
# 	print v1
	

def send_sms(mobile_number,text):
	print mobile_number
	print text
	# headers = {'Content-Type':'application/json'}
	# data = {'user':settings.SMS_USER, 'pass':settings.SMS_PASSWORD,'sender':settings.SMS_SENDER,'phone':mobile_number,'text':text,'priority':settings.SMS_PRIORITY,'stype':settings.SMS_STYPE}
	# r = requests.post('http://dnd.blackholesolution.com/api/sendmsg.php', headers=headers, params=data)