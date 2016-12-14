from django.contrib import admin

# Register your models here.
from listings.models import Listings

admin.site.register(Listings)
