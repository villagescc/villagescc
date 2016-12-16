from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categories(models.Model):
    categories_text = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.categories_text)


class SubCategories(models.Model):
    categories = models.ForeignKey(Categories)
    sub_categories_text = models.CharField(max_length=220)

    def __str__(self):
        return "{}".format(self.sub_categories_text)
