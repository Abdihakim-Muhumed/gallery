from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)
    def _str_(self):
        return self.name
class Location(models.Model):
    name = models.CharField(max_length =30)
    def _str_(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =150)
    category = models.ManyToManyField(Category)
    location = models.ManyToManyField(Location)

    def _str_(self):
        return self.name
        