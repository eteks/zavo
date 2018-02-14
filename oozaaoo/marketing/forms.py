from django import forms
from marketing.models import Marketing, AccomodationType

class MarketingForm(forms.ModelForm):
	class Meta():
		model = Marketing
		fields = '__all__'


# class combinedForm(accomodationTypeForm):
# 	class Meta(accomodationTypeForm.Meta):
# 		model = combined
# 		# exclude = ()