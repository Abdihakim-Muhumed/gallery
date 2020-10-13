from django.shortcuts import render
from .models import Photos,Category,Location
# Create your views here.

def home(request):
    photos = Photos.objects.all()

    return render(request,'index.html',{"photos":photos})

def search_photo(request):
    if 'category' in request.GET and request.GET["category"]:
        search_category = request.GET.get("category")
        searched_photos = Photos.search_by_category(search_category)
        message = f"{search_category}"
        return render(request,'search.html',{"searched_photos":searched_photos, "message":message})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})

def photo(request,photo_id):
    try:
        photo = Photos.get_photo_by_id(photo_id)
    except DoesNotExist:
        raise Http404()

    return render(request,'photo.html',{"photo":photo})
