from django.test import TestCase
from .models import Photos,Category,Location
# Create your tests here.
class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        new_location = 'Kwetu'
        self.location.update_location(self.location.pk, new_location)
        newlocation = Location.objects.filter(name='Kwetu')
        self.assertTrue(len(newlocation) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class TestCategory(TestCase):

    def setUp(self):
        self.category = Category(name='Personal')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_update_category(self):
        new_category = 'Travel'
        self.category.update_category(self.category.pk, new_category)
        newcategory = Category.objects.filter(name='Travel')
        self.assertTrue(len(newcategory) > 0)
    

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class TestPhotos(TestCase):

    #set up
    def setUp(self):
        self.newCategory = Category(name='Travel')
        self.newCategory.save_category()
        self.newLocation = Location(name='Nairobi')
        self.newLocation.save_location()
        
        self.newImage = Photos(name = 'First image',description = 'This is the first image.')

        self.newImage.save_photo()
        self.newImage.category.add(self.newCategory)
        self.newImage.location.add(self.newLocation)

    def tearDown(self):
        Photos.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.newImage, Photos))

    def test_delete_photo(self):
        self.newImage.delete_photo()
        photos = Photos.objects.all()
        self.assertTrue(len(photos) == 0)


    def test_get_photo_by_id(self):
        res = self.newImage.get_photo_by_id(self.newImage.id)
        photo = Photos.objects.filter(id=self.newImage.id)
        self.assertTrue(res, photo)

    def test_filter_photo_by_location(self):
        self.newImage.save_photo()
        res = self.newImage.filter_by_location(location='Nairobi')
        self.assertTrue(len(res) == 1)

    def test_search_photo_by_category(self):
        self.newImage.save_photo()
        res = self.newImage.search_by_category(category='Travel')
        self.assertTrue(len(res) > 0)

    
