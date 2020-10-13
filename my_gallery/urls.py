from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('',views.home, name = 'Home'),
    url('^search/',views.search_photo, name = 'search_photo'),
    url(r'^photo/(\d+)',views.photo,name ='photo')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
