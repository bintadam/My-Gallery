from email.mime import image
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


def picture(request, past_date):
    try:
        image = Image.objects.get(id = image_id)
    except OjectDoesNotExit :
        
        raise Http404()
    return render (request, 'all-pictures/pictures.html', {"image": image}) 


def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = pictures.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
