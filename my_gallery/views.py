from django.shortcuts import render
from .models import Photos,Category,Location
from django.http import HttpResponse, Http404
# Create your views here.

def home(request):
    photos = Photos.objects.all()
    return render(request,'index.html',{"photos":photos})

def search_photo(request):
    if 'category' in request.GET and request.GET["category"]:
        search_category = request.GET.get("category")
        searched_photos = Photos.search_by_category(search_category)
        message = f"{search_category}"
        title = "Search photo"
        return render(request,'search.html',{"searched_photos":searched_photos, "message":message, "title":title})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})

def photo(request,photo_id):
    try:
        photo = Photos.objects.get(id=photo_id) 
        title = "Photo"
    except :
        raise Http404()

    return render(request,'photo.html',{"photo":photo,"title":title})
