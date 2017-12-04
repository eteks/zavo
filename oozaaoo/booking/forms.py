from django import forms
from booking.models import Booking
print "forms entered"
# class BookingForm( forms.ModelForm ):
class BookingForm(forms.ModelForm):
	class Meta:
		model=Booking
		fields= ['contactMobile','contactMail']

	def clean_contactMail(self):
		# print "clean_contactMail"
		contactMail= self_cleaned_data.get('contactMail')
		contactMail_base, provider = contactMail.split("@")
		domain, extension = provider.split('.')
		if not extension =="edu":
			raise forms.ValidationError("Use EDU")		
		return contactMail


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