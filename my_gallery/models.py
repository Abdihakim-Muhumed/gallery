from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)
    def _str_(self):
        return self.name
    @classmethod
    def update(cls, pk, category):
        cls.objects.filter(pk=pk).update(name=category)

    def save(self):
         self.save()

    def delete(self):
        self.delete()
class Location(models.Model):
    name = models.CharField(max_length =30)
    def _str_(self):
        return self.name

class Photos(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =150)
    category = models.ManyToManyField(Category)
    location = models.ManyToManyField(Location)
    image = models.ImageField(upload_to='Photos/')

    def _str_(self):
        return self.name
