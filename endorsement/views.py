from django.shortcuts import render

# Create your views here.
def endorsement(request):
	return render(request, 'endorsement/endorsement.html')
