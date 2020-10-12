from django.conf.urls import urls
from . import views

urlpatterns=[
    url('',views.home, name = 'Home'),
]