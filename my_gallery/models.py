from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)
    def _str_(self):
        return self.name