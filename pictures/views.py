from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Image

from pictures.models import Image

# Create your views here.
def welcome(request):
    return render (request, 'welcome.html')



def pictures(request):
    
    images = Image.display_all_images()

    return render(request, 'all-pictures/pictures.html', {"images":images},)


def picture(request, image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist :
        
        raise Http404()
    return render (request, 'all-pictures/pictures.html', {"image": image}) 


def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        category = request.GET.get("picture")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)

        return render(request, 'all-pictures/search.html',{"message":message,"images": searched_images})

    else:
        message = "No results available"
        return render(request, 'all-pictures/search.html',{"message":message})
