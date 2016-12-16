from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Categories Models
from categories.models import SubCategories

# Create your models here.
class Listings(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=220)
    price = models.FloatField()
    subcategories = models.ForeignKey(SubCategories, null=True, blank=True)

    OFFER = 'Offer'
    REQUEST = 'Request'
    TEACH = 'Teach'
    LEARN = 'Learn'
    GIFT = 'Gift'
    GOAL = 'Goal'
    LISTING_TYPE = (
        ('OF', OFFER),
        ('RQ', REQUEST),
        ('TC', TEACH),
        ('LR', LEARN),
        ('GT', GIFT),
        ('GL', GOAL)
    )
    listing_type = models.CharField(max_length=2, choices=LISTING_TYPE)
    photo = models.ImageField(upload_to='media')
