from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.

MEAL_PLAN = (
		('breakfast', 'BREAKFAST'),
		('lunch', 'LUNCH'),
		('dinner','DINNER')
	)
MEAL_PLAN_TYPE = (
		('ep', 'EP'),
		('cp', 'CP'),
		('map','MAP'),
		('ap','AP')
	)
PAYMENT_MODE = (
	('online','ONLINE'),
	('cheque/dd','CHEQUE/DD'),
	('cash','CASH')
)

#Master model to use in throughout website
class AbstractDefault(models.Model):
	active_status = models.BooleanField(verbose_name = 'Active Status', default = False)
	delete_status = models.BooleanField(verbose_name = 'Delete status', default = False)
	created_date = models.DateTimeField(help_text="Auto generated by system.", default = datetime.now)
	modified_date = models.DateTimeField(help_text="Auto generated by system.", default = datetime.now)

	class Meta:
		abstract = True

class AccomodationType(AbstractDefault):
	accomodation_type = models.CharField(verbose_name = 'Accomodation Type', max_length = 50)

	def __str__(self):
		return self.accomodation_type

class AccomodationStar(AbstractDefault):
	accomodation_star = models.CharField(verbose_name = 'Accomodation in Star Hotel', max_length = 50)
	accomodation_type = models.ManyToManyField(AccomodationType, verbose_name = 'Accomodation Type',through='AccomodationStarAndType')

	# def __str__(self):
	# 	accomo = self.accomodation_star + self.accomodation_type
	# 	return unicode(accomo)
	def __unicode__(self):
		return unicode(self.accomodation_star)

class AccomodationStarAndType(models.Model):
    """A FamilyChild is the many-to-many intersection of Families and Children"""
    accomodation_type = models.ForeignKey('AccomodationType')
    accomodation_star = models.ForeignKey('AccomodationStar')
    active_status = models.BooleanField(verbose_name = 'Active Status', default = False)
    delete_status = models.BooleanField(verbose_name = 'Delete status', default = False)

    def __unicode__(self):
		return '%s - %s' % (self.accomodation_star, self.accomodation_type)

class ModeOfTransport(AbstractDefault):
	transport_mode = models.CharField(verbose_name = "Mode of Transport Type", max_length = 50)

	def __str__(self):
		return self.transport_mode

class TransportType(AbstractDefault):
	transport_type = models.CharField(verbose_name = "Transport Type", max_length = 100)
	transport_mode = models.ManyToManyField(ModeOfTransport, verbose_name = 'Transport Mode',through = 'TransportModeAndType')
	
	def __str__(self):
		return self.transport_type

class TransportModeAndType(models.Model):
    """A FamilyChild is the many-to-many intersection of Families and Children"""
    transportMode = models.ForeignKey('ModeOfTransport')
    transportType = models.ForeignKey('TransportType')
    active_status = models.BooleanField(verbose_name = 'Active Status', default = False)
    delete_status = models.BooleanField(verbose_name = 'Delete status', default = False)

    def __str__(self):
		return '%s - %s' % (self.transportMode, self.transportType)
