from django import forms
from marketing.models import Marketing, AccomodationType
from models import Payment

class PaymentForm(forms.ModelForm):
	# total_amount = forms.CharField(disabled=True,initial='0')
	# balance_amount = forms.CharField(disabled=True,initial='0')

	def __init__(self, *args, **kwargs):
		super(PaymentForm, self).__init__(*args, **kwargs)
		self.fields['total_amount'].widget.attrs['readonly'] = True
		self.fields['balance_amount'].widget.attrs['readonly'] = True

	class Meta():
		model = Payment
		fields = '__all__'