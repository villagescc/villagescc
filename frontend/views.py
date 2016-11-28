from django.shortcuts import render


# Create your views here.
def home(request):
	"""
	This is home page but before logged in user will see this pages
	returns before login home.
	url: /home
	"""
	return render(request, 'pages/home.html')


def profile(request):
	return render(request, 'pages/profile.html')
