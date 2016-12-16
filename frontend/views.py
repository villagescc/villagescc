from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

# Forms
from listings.forms import ListingsForms

# models
from listings.models import Listings
from categories.models import Categories


# Create your views here.
def home(request):
    """
    This is home page but before logged in user will see this pages
    returns before login home.
    url: /home
    """
    # POST Request
    if request.method == 'POST':
        form = ListingsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('frontend:home'))
        else:
            print form.errors

    # GET Request
    listings = Listings.objects.all()
    form = ListingsForms()
    categories = Categories.objects.all()
    return render(request, 'frontend/home.html',{
        'listings': listings,
        'form': form,
        'categories': categories})
