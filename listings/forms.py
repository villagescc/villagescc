from django.forms import ModelForm

# Import App Model
from listings.models import Listings


# Forms
class ListingsForms(ModelForm):
    class Meta:
        model = Listings
        fields = '__all__'
