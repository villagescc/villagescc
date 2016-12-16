from django.forms import ModelForm
from django.forms.widgets import Select, NumberInput

# Import App Model
from listings.models import Listings

# Forms
class ListingsForms(ModelForm):
    class Meta:
        model = Listings
        fields = '__all__'
        widgets = {
            'listing_type': Select(attrs={
                'class': 'form-control input-lg',
                'style': 'width: 100%;'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control'
            }),
            'subcategories': Select(attrs={
                'class': 'form-control'
            })
        }
