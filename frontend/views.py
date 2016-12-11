from django.shortcuts import render


# Create your views here.
def home(request):
	"""
	This is home page but before logged in user will see this pages
	returns before login home.
	url: /home
	"""
	listings = [1,2,3,4,5,5]
	return render(request, 'frontend/home.html', {'listings': listings})
