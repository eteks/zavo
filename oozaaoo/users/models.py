from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from oozaaoo.constant import USER_TYPE


# Create your models here.

class Users(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mobileNumber = models.CharField(verbose_name = 'Mobile Number', max_length = 255)

	def __str__(self):
		return self.user.username
