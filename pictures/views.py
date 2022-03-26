from email.mime import image
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

from pictures.models import Image

# Create your views here.
def welcome(request):
    return render (request, 'welcome.html')



def pictures(request):
    image = Image.display_all_images()

    return render(request, 'all-pictures/pictures.html', {"images:images"},)