from django.shortcuts import render
from booking.models import Booking
from django.http import HttpResponse,JsonResponse

# Create your views here.
def total_amount_generation(request):
	print "total_amount_geneation"
	print request.POST['booking_id']
	try:
		check_id = Booking.objects.get(booking_id__exact=request.POST['booking_id'])
	except Booking.DoesNotExist:
		check_id = None
	if check_id is not None:		
		results = {'total_cost':check_id.total_cost,'balance_amount':check_id.total_cost-check_id.paid_amount}
	else:		
		results = {}
	return JsonResponse(results)

def get_package_details(request):
	print "get_package_details"
	print request.POST['package_id']
	try:
		check_id = Tourpackage.objects.get(id=request.POST['package_id'])
		package_cost = (request.POST['adult'] * check_id.adult_cost) + (request.POST['children'] * check_id.children_cost) + (request.POST['adult'] * check_id.infant_cost)
	except Tourpackage.DoesNotExist:
		check_id = None
	if check_id is not None:		
		results = {'package_cost':check_id.package_cost,'balance_amount':check_id.total_cost-check_id.paid_amount}
	else:		
		results = {}
	return JsonResponse(results)