from django import forms
from booking.models import Booking
from django.core.exceptions import ValidationError
import datetime
# class BookingForm( forms.ModelForm ):
# class BookingForm(forms.ModelForm):
# 	class Meta:
# 		model=Booking
# 		fields= ['package_Name', 'contactAddress', 'contactMobile','contactMail', 'dateDeparture', 'dateArrival', 'duration', 'totalPersons', 'adultPersons', 'childPersons', 'infantPersons', 'accomodationType', 'accomodationStar', 'modeOfTransport', 'mealPlan', 'modePayment', 'notes',]
# 		dateDeparture = forms.DateField()
# 	def clean_contactMail(self):
# 		# print "clean_contactMail"
# 		contactMail= self.cleaned_data.get('contactMail')
# 		contactMail_base, provider = contactMail.split("@")
# 		domain, extension = provider.split('.')
# 		if not extension =="edu":
# 			raise forms.ValidationError("Use EDU")	
# 		return contactMail

# 	def clean_contactMobile(self):
# 	    contactMobile = self.cleaned_data.get('contactMobile')
# 	    try:
# 	        if long(contactMobile) and not contactMobile.isalpha():
# 	            min_length = 10
# 	            max_length = 13
# 	            ph_length = str(contactMobile)
# 	            if len(ph_length) < min_length or len(ph_length) > max_length:
# 	                raise ValidationError('Phone number length not valid')

# 	    except (ValueError, TypeError):
# 	        raise ValidationError('Please enter a valid phone number')
# 	    return contactMobile


    # def clean_dateDeparture(self):
    #     date = self.cleaned_data['dateDeparture']
    #     if dateDeparture < datetime.dateDeparture.today():
    #         raise forms.ValidationError("The date cannot be in the past!")
    #     return dateDeparture

    # contactMail = forms.EmailField(label=_("Email"))
    # contactMail = forms.CharField( 
    #     label = _('Email'),
    #     max_length = 50,
    #     widget = forms.Textarea(
    #         attrs = {'rows': 6, 'cols': 60, 'readonly': True}
    #     ),
    #     required = False,
    # )

    # accomodationType = forms.ChoiceField( 
    #     widget = forms.Select(),
    #     required = False,
    #     choices = actor_tuple,
    # )
    # accomodationStar = forms.ChoiceField( 
    #     widget = forms.Select(),
    #     required = False,
    #     choices = actor_tuple,
    # )
    # modeOfTransport = forms.ChoiceField( 
    #     widget = forms.Select(),
    #     required = False,
    #     choices = actor_tuple,
    # )
    # mealPlan = forms.ChoiceField( 
    #     widget = forms.Select(),
    #     required = False,
    #     choices = actor_tuple,
    # )
    # modePayment = forms.ChoiceField( 
    #     widget = forms.Select(),
    #     required = False,
    #     choices = actor_tuple,
    # )