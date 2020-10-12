from django.contrib import admin

# Register your models here.
from .models import Category,Location,Photos

class PhotosAdmin(admin.ModelAdmin):
    filter_horizontal =('location','category')


admin.site.register(Photos,PhotosAdmin)
admin.site.register(Category)
admin.site.register(Location)