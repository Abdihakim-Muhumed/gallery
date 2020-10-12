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
    
    def save(self):
        self.save()

    def delete(self):
        self.delete()

    @classmethod
    def update(cls, pk, location):
        cls.objects.filter(pk=pk).update(name=location)

    @classmethod
    def get_location(cls):
        locations = Location.objects.all()
        return locations



class Photos(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =150)
    category = models.ManyToManyField(Category)
    location = models.ManyToManyField(Location)
    image = models.ImageField(upload_to='Photos/')

    def _str_(self):
        return self.name

    @classmethod
    def search_by_category(cls, category):
        photos = cls.objects.filter(category_name_icontains=category)
        return photos

    @classmethod
    def update_photo(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_photo_by_id(cls, id):
        photo = cls.objects.filter(id=id).all()
        return photo

    @classmethod
    def filter_by_location(cls, location):
        photo = Photos.objects.filter(location__name=location).all()
        return photo

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()