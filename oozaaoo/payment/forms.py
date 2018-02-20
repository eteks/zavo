from django import forms
from marketing.models import Marketing, AccomodationType
from models import Payment

class PaymentForm(forms.ModelForm):
	total_amount = forms.CharField(disabled=True,initial='0')
	balance_amount = forms.CharField(disabled=True,initial='0')

	class Meta():
		model = Payment
		fields = '__all__'